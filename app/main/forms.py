from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from flask import flash
from flask_wtf import Form
from ..models import Message, User, Farmer
from wtforms import SubmitField, SelectField, StringField, TextAreaField, IntegerField, BooleanField, HiddenField
from wtforms.validators import Required, Length, ValidationError, Regexp, Email, NumberRange




class AddFarmersForm(Form):
    farmers_name = StringField("Farmers Name",validators=[Required(), Length(8, 50)])
    phone_no = IntegerField("Phone Number")
    farmers_id_no = IntegerField("Farmers id_no")
    gender = SelectField("Gender", choices=[('M','Male'), ('F','Female')])
    location = SelectField("County", choices=[('Nai','Nairobi'),('Nax','Nakuru'),('ksmu','Kisumu'),('Eld','Eldoret'),('Kymbu','Kiambu'),('Macha','Machakos')])
    type_of_farming= SelectField("what do you grow?", choices=[('c-p','cash-crop'),('l-f','Livestock-farming'),('s-f','Subsistence-farming')])
    submit = SubmitField("Submit")



    
class SendMessageForm(Form):
    to = SelectField("to", coerce=int)
    farmers_name=StringField("Farmers Name")
    message = TextAreaField("message")
    
    submit = SubmitField("submit")


    def __init__(self, *args, **kwargs):

        super(SendMessageForm, self).__init__(*args, **kwargs)
        self.to.choices = [
          (i.id, i.phone_no) for i in Farmer.query.order_by(Farmer.phone_no).all()
        ]

        gateway = AfricasTalkingGateway("Kunene","be141cfbfa9cf4ac79d6784ef3cf41e88a542ccf9757b93125724bdbfe23c238")
        submit = gateway.sendMessage("to", "message")   

   
    #print to, message
        


   

  