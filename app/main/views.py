
from app.decorators import admin_required
from app.request import get_quotes
from flask import render_template
from . import main
from ..decorators import  admin_required,permission_required
from flask_login import login_required

from ..models import Permission



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


@main.route('/admin')
@login_required
@admin_required
def from_admins_only():
   return 'for Admins only'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
   return 'For comment moderation'


@main.route('/write_articles')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def create_blog():
   return 'For comment moderation'
