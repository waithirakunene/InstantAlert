from flask import render_template, url_for, redirect, abort, flash, request, current_app
from flask_login import login_required, current_user
from app import db
from app.main import main
from ..models import User, Message
from app.main.forms import (
   SendMesssageForm
)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form =  SendMesssageForm()
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






