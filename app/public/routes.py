from flask import Flask, url_for, redirect, render_template, current_app, flash
from app.public import bp

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('public/index.html', title='Home')