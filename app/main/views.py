from flask import render_template, url_for, redirect, abort, flash, request, current_app
from flask_login import login_required, current_user
from app import db
from app.main import main
from ..models import User, Message, Farmer
from app.main.forms import (
   SendMessageForm, AddFarmersForm
)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form =  SendMessageForm()
    if current_user.is_admin:
        if form.validate_on_submit():
            message = Message( 
                    send_to = form.message.data,
                    message_body= form.message_body.data,
                    
                    )
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
                farmers_id_no=form.farmers_id_no.data,
                gender=form.gender.data,
                location=form.location.data,
                type_of_farming=form.type_of_farming.data
                
            )

            db.session.add(farmer)
            db.session.commit() 
            return redirect(url_for('main.index'))    
            flash('New farmer added.')
    return render_template('main/add_farmer.html', form=form)
      

