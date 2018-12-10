# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/12/7
"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app
from application import db
from application.models import User, Post


manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
