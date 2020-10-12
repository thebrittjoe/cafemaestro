from flask import Flask, url_for, redirect, render_template, current_app, flash
from app.manager import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('manager/index.html', title='Management Portal')