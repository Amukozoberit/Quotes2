from flask_wtf import  FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class CommentsForm(FlaskForm):
    comment=TextAreaField('comment',validators=[Required()])
    submit=SubmitField('submit')

class MailSub(FlaskForm):
    mail=StringField('Mail')
    submit=SubmitField('submit')

