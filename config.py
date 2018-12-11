# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/12/7
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 15
    LANGUAGES = ['en', 'es']
    # 配置邮件服务器
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.exmail.qq.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1 is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'pengfei.zhang@worldfarm.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '8023.zpfZZ'
    ADMINS = ['pengfei.zhang@worldfarm.com']
