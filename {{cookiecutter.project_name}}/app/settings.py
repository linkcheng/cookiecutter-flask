# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import yaml
from environs import Env

env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'

CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 日志目录
LOG_DIR = './logs'

# 日志保留数量
LOG_BACKUP_COUNT = 30

# 日志分割类型 ['time', 'size']
LOG_ROTATING_FILE_MODE = 'time'

# sentry
SENTRY_DSN = env.str('SENTRY_DSN', default='')

# 数据库配置文件
DATABASE_CONFIG_FILE = env.str('DATABASE_CONFIG_FILE', default='')

# 数据库配置
if DATABASE_CONFIG_FILE:
    with open(DATABASE_CONFIG_FILE, 'r', encoding='utf-8') as f:
        DB_CONFIG = yaml.load(f.read())
