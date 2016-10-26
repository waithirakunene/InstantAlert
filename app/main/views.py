from AfricasTalkingGateway import AfricasTalkingGateway
from flask import render_template, url_for, redirect, abort, flash, request, current_app, jsonify
from flask_login import login_required, current_user
from app import db
from app.main import main
from ..models import User, Message, Farmer
from app.main.forms import SendMessageForm, AddFarmersForm
   

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form =  SendMessageForm()
    if form.validate_on_submit():
        message = Message(
                to = form.to.data,
                farmers_name = form.farmers_name.data,
                message = form.message.data
            )

        print form.to.data, form.message.data
        gateway = AfricasTalkingGateway("Kunene","be141cfbfa9cf4ac79d6784ef3cf41e88a542ccf9757b93125724bdbfe23c238")
        gateway.sendMessage(str(form.to.data), form.message.data)

        db.session.add(message)
        db.session.commit()
        return redirect(url_for('main.index'))
        flash('Message Sent')

    return render_template('main/message.html', form=form)


@main.route('/add_farmer', methods=['GET','POST'])
@login_required
def add_farmer():
    form = AddFarmersForm()
    if form.validate_on_submit():
            farmer = Farmer(
                farmers_name=form.farmers_name.data,
                phone_no = form.phone_no.data,
                farmers_id_no=form.farmers_id_no.data,
                gender=form.gender.data,
                location=form.location.data,
                type_of_farming=form.type_of_farming.data
                
            )

            db.session.add(farmer)
            db.session.commit() 
              
            flash('New farmer added.')
            return redirect(url_for('main.add_farmer')) 
    return render_template('main/add_farmer.html', form=form)


@main.route('/view-messages')
@login_required
def view_messages():
    
    messages = Message.query.all()

    return render_template('main/view_messages.html', messages=messages)  