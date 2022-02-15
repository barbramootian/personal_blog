from flask import render_template,redirect,request,url_for,flash
from . import auth
from ..email import mail_message
from .forms import RegistrationForm,LoginForm
from ..models import User,Post
from .. import db
from flask_login import login_user,logout_user,login_required

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)  


@auth.route('/login',methods = ["GET","POST"])
def login():
    """Login view function"""
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    return render_template('auth/login.html', login_form=login_form) 