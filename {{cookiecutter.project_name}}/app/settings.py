# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False

LOG_DIR = './logs'
LOG_BACKUP_COUNT = 30
LOG_ROTATING_FILE_MODE = 'time'

SENTRY_DSN = ''

DATABASE_CONFIG_FILE = env.str('DATABASE_CONFIG_FILE')
