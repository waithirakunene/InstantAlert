from flask_wtf import Form
from ..models import Message, User, Farmer
from wtforms import SubmitField, SelectField, StringField, TextAreaField, IntegerField, BooleanField, HiddenField
from wtforms.validators import Required, Length, ValidationError, Regexp, Email, NumberRange


class AddFarmersForm(Form):
    farmers_name = StringField("Farmers Name",validators=[Required(), Length(8, 50)])
    phone_no = IntegerField("Phone Number")
    farmers_id_no = IntegerField("Farmers id_no")
    gender = SelectField("Gender", choices=[('M','Male'), ('F','Female')])
    location = SelectField("County", choices=[('Nai','Nairobi'),('Mu','Muranga'),('Nax','Nakuru'),('ksmu','Kisumu'),('Eld','Eldoret'),('Kymbu','Kiambu'),('Macha','Machakos')])
    type_of_farming= SelectField("what do you grow?", choices=[('c-p','Tea-Bushes'),('l-f','Livestock-farming'),('s-f','Subsistence-farming')])
    submit = SubmitField("Submit")


class SendMessageForm(Form):
    to = SelectField("Send_To", coerce=int)
    farmers_name = StringField("Confirm Farmers Name")
    message = TextAreaField("Message")
    
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.to.choices = [
          (i.phone_no, i.farmers_name) for i in Farmer.query.order_by(Farmer.phone_no).all()
        ]

