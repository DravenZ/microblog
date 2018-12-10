# encoding: utf-8

"""
__author__ = "Zhang Pengfei"
__date__ = 2018/12/10
"""


from flask import render_template
from application import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
