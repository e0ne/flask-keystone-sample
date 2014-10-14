# -*- config:utf-8 -*-

from datetime import timedelta

project_name = "yourprojectname"


class Config(object):
    # use DEBUG mode?
    DEBUG = False

    # use TESTING mode?
    TESTING = False

    # use server x-sendfile?
    USE_X_SENDFILE = False

    # DATABASE CONFIGURATION
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_dev.sqlite" % project_name
    SQLALCHEMY_ECHO = False

    CSRF_ENABLED = True
    SECRET_KEY = "secret"  # import os; os.urandom(24)
    LOGGER_NAME = "%s_log" % project_name
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)

    # EMAIL CONFIGURATION
    MAIL_SERVER = "localhost"
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_DEBUG = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    DEFAULT_MAIL_SENDER = "example@%s.com" % project_name

    # ex: BLUEPRINTS = ['blog.views.app']  # where app is a Blueprint instance
    # ex: BLUEPRINTS = [('blog.views.app', {'url_prefix': '/myblog'})]
    # where app is a Blueprint instance
    BLUEPRINTS = ['flaskkeystone.views.app']

    # Keystone params
    OS_CACERT = None
    OS_CERT = None
    INSECURE = False
    OS_AUTH_URL = 'http://192.168.122.22:5000'
    OS_USERNAME = 'admin'
    OS_PASSWORD = '123'
    OS_USER_DOMAIN_NAME = None
    OS_USER_DOMAIN_ID = None
    OS_PROJECT_ID = 'ee7d1c4db76a4de088b1cb694cb6524a'
    OS_PROJECT_NAME = 'admin'
    OS_TENANT_ID = 'ee7d1c4db76a4de088b1cb694cb6524a'
    OS_TENANT_NAME = 'admin'


class Dev(Config):
    DEBUG = True
    MAIL_DEBUG = True
    SQLALCHEMY_ECHO = True


class Testing(Config):
    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/%s_test.sqlite" % project_name
    SQLALCHEMY_ECHO = False


class Staging(Config):
    pass


class Production(Config):
    pass

