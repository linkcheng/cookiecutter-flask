#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import logging.config

from app.settings import LOG_DIR
from app.settings import LOG_BACKUP_COUNT
from app.settings import LOG_ROTATING_FILE_MODE
from config.APP import SENTRY_DSN


logger = logging.getLogger('log')

default_logging_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s '
                      '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        # # If you're actually catching an exception, use `exc_info=True`
        # logger.error('There was an error, with a stacktrace!', exc_info=True)
        #
        # # If you don't have an exception, but still want to capture a
        # # stacktrace, use the `stack` arg
        # logger.error('There was an error, with a stacktrace!', extra={
        #     'stack': True,
        # })
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
        },
    },

    'loggers': {
        '': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry'],
            'propagate': False
        },
    },

    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'sentry', 'info_file_handler', 'error_file_handler']
    }
}

time_info_file_handler = {
    'class': 'logging.handlers.TimedRotatingFileHandler',
    'level': 'INFO',
    'formatter': 'simple',
    'when': 'D',
    'encoding': 'utf8',
    'backupCount': LOG_BACKUP_COUNT,
}

time_error_file_handler = {
    'class': 'logging.handlers.TimedRotatingFileHandler',
    'level': 'ERROR',
    'formatter': 'simple',
    'when': 'D',
    'encoding': 'utf8',
    'backupCount': LOG_BACKUP_COUNT,
}


size_info_file_handler = {
    'class': 'logging.handlers.RotatingFileHandler',
    'level': 'INFO',
    'formatter': 'simple',
    # 当达到 250MB 时分割日志
    'maxBytes': 262144000,
    # 最多保留 100 份文件
    'backupCount': LOG_BACKUP_COUNT,
    'encoding': 'utf8'
}

size_error_file_handler = {
    'class': 'logging.handlers.RotatingFileHandler',
    'level': 'ERROR',
    'formatter': 'simple',
    'maxBytes': 262144000,
    'backupCount': LOG_BACKUP_COUNT,
    'encoding': 'utf8'
}


def configure_logging(log_path=LOG_DIR):
    if not os.path.exists(log_path):
        os.mkdir(log_path)

    info_file_name = os.path.join(log_path, 'info.log')
    error_file_name = os.path.join(log_path, 'error.log')

    if LOG_ROTATING_FILE_MODE == 'size':
        info_file_handler = size_info_file_handler
        error_file_handler = size_error_file_handler
    else:
        info_file_handler = time_info_file_handler
        error_file_handler = time_error_file_handler

    info_file_handler.update(filename=info_file_name)
    error_file_handler.update(filename=error_file_name)

    default_logging_config['handlers']['info_file_handler'] = info_file_handler
    default_logging_config['handlers']['error_file_handler'] = error_file_handler
    logging.config.dictConfig(default_logging_config)


if __name__ == '__main__':
    configure_logging()
    logger = logging.getLogger('logger')
    logger.info('test logger')
