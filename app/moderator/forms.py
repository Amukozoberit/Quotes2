
from gettext import bind_textdomain_codeset
from flask_wtf import Form
from wtforms import BooleanField,StringField,PasswordField,validators

from wtforms.fields.simple import SubmitField, TextAreaField
class RegisterArticle(Form):
    article_body=TextAreaField('Article',[validators.length(min=50,max=1000)])
    title=StringField('Title',[validators.length(min=10,max=200)])
    video=StringField('video embed code (450 pix wide')
   
    submit=SubmitField('submit')







class Comment(Form):
    comments=StringField('comment',[validators.Required()])
    submit=SubmitField('submit')