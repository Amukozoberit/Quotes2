
from flask import render_template
from . import main



#views

@main.route('/')
def index():
    return render_template('authtemplates/index.html')


@main.route('/')
def profile():
    return render_template('authtemplates/profile.html')