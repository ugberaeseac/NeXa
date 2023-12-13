#!/usr/bin/python3
"""

"""


from flask import render_template, flash, redirect, url_for, request
from nexa import app
from nexa import db
from nexa import bcrypt
from nexa.form import RegistrationForm, LoginForm
from nexa.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required


posts=[{
	'name': 'Ugberaese Charles',
	'username': 'charlyn',
	'content': 'NeXa is the ultimate social network for ALX students and alumni',
	'posted_at': '2023-12-12 10:49:32.145223'
	},
	{
	'name': 'Akanni Williams',
	'username': 'akanni',
	'content': 'I had a similar thing happen to me couple months back lol, Not a nice experience lol',
	'posted_at': '2023-12-12 10:50:11.032323'
	},
	{
	'name': 'Mounssif nuuX BOUHLAOUI',
	'username': 'nuuxcode',
	'content': 'If ur discord is affected go to Authorized Apps and delete everything u dont know..',
	'posted_at': '2023-12-12 10:52:42.243398'	
	},
	{
	'name': 'Sabah Hasbi',
	'username': 'sabah',
	'content': 'Need help with python? send a DM',
	'posted_at': '2023-12-12 11:09:01.500432'	
	}
	]


@app.route('/')
@app.route('/about')
def index():
    """
    landing page
    """
    return render_template('index.html')

@app.route('/home')
def home():
    """
    home page displayed when a user is logged in
    """
    if current_user.is_authenticated:
        return render_template('home.html', posts=posts)
    else:
        return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    signup to create an account
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                 form.password.data).decode('utf-8')
        user = User(name=form.name.data, username=form.username.data,
                 password=hashed_password, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    logs in the user
    """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    form.email(placeholder='Email address')
    form.password(placeholder='Password')
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check email or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """
    logs out the user
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """

    """
    return render_template('settings.html')
