#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import json
from datetime import datetime
from flask import request
from raven.utils.wsgi import get_environ, get_headers

try:
    from app.settings import SENTRY_DSN
except ImportError:
    SENTRY_DSN = None


client = None
if SENTRY_DSN:
    from raven.contrib.flask import Sentry
    client = Sentry(dsn=SENTRY_DSN)


def get_request_info(req=None):
    """
    获取 req 请求相关信息：host、url、http method、headers、http environment
    :param req:
    :return:
    """
    if not req:
        req = request

    headers = dict(get_headers(req.environ))
    request_info = {
        'host': req.host_url,
        'url': req.url,
        'method': req.method,
        'headers': headers,
        'env': dict(get_environ(req.environ)),
    }
    try:
        body = json.loads(req.data)
        request_info.update({'data': json.dumps(body)})
    except Exception as e:
        pass
    return request_info


def get_env_info():
    """
    获取默认环境变量信息，作为tags、extra、request参数
    :return:
    """
    try:
        req = get_request_info()
    except RuntimeError:
        req = {}

    env_info = {
        'tags': {},
        'request': req
    }

    return env_info


def track(message=None, level='error', **kwargs):
    """
    跟踪接口，根据是否存在 sys.exc_info()判断 使用captureMessage 或 captureException
    :param message: error消息描述
    :param level: 同 sentry 一致，默认为 error 级别
    :param kwargs: dicts， 其它接口信息，支持 extra, tags, request 等等
    :return:
    """
    if not client:
        return

    exc_info = sys.exc_info()
    data = get_env_info()

    # 如果存在异常信息，则调用 captureException 跟踪堆栈
    if exc_info[0]:
        exc_type = exc_info[1].__class__.__name__

        data['tags']['type'] = exc_type
        client.captureException(exc_info=exc_info, level=level, data=data, **kwargs)
    else:
        # 如果 message 为空，则为 captureMessage 生成一个 message
        if not message:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f'{client.name}, {timestamp}'
        client.captureMessage(message, level=level, data=data, **kwargs)


def track_debug(message=None, **kwargs):
    return track(message=message, level='debug', **kwargs)


def track_info(message=None, **kwargs):
    return track(message=message, level='info', **kwargs)


def track_warn(message=None, **kwargs):
    return track(message=message, level='warning', **kwargs)


def track_error(message=None, **kwargs):
    return track(message=message, **kwargs)
