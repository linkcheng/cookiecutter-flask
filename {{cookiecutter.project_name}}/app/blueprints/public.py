#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import logging
from flask import Blueprint

logger = logging.getLogger(__name__)
public_pb = Blueprint('public', __name__)


@public_pb.route('/')
def index():
    return 'It works.'


@public_pb.route('/error')
def error():
    raise ValueError('This is a ValueError!')


@public_pb.route('/log_error')
def log_error():
    try:
        1 / 0
    except ZeroDivisionError as e:
        logger.error(f'This is a log error, exp:{e}!', exc_info=True)
