
from app.request import get_quotes
from flask import render_template
from . import main






#views

@main.route('/')
def index():
   hello="Welcome to quotes center we have you"
   quotes=get_quotes()
   print(quotes)
   return render_template('maintemplates/index.html',hello=quotes)


@main.route('/')
def profile():
    return render_template('authtemplates/profile.html')