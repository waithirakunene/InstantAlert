from flask import flash
from flask_wtf import Form
from ..models import Message, User
from wtforms import SubmitField, SelectField, StringField, TextAreaField, IntegerField, BooleanField, HiddenField
from wtforms.validators import Required, Length, ValidationError, Regexp, Email, NumberRange


class SendMesssageForm(Form):
    username = SelectField("Send_To", coerce=int)
    message = TextAreaField("Message")
    
    submit = SubmitField("Submit")


    def __init__(self, *args, **kwargs):
        super(SendMesssageForm, self).__init__(*args, **kwargs)
        self.username.choices = [
            (i.id, i.username) for i in User.query.order_by(User.username).all()
        ]