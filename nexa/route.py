#!/usr/bin/python3
"""

"""


from flask import render_template, flash, redirect, url_for, request
from nexa import app
from nexa import db
from nexa import bcrypt
from nexa.form import RegistrationForm, LoginForm, UpdateForm
from nexa.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
import secrets

"""
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
"""

@app.route('/')
@app.route('/about')
def index():
    """
    landing page
    """
    return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    home page displayed when a user is logged in
    """
    if current_user.is_authenticated:
        if request.method == 'POST':
            content = request.form.get('content')
            user_id = current_user.id
            new_post = Post(content=content, user_id=user_id)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('home'))

        posts = Post.query.order_by(Post.posted_at.desc()).all()
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
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(
                 request.form.get('password')).decode('utf-8')
        name = f"{request.form.get('first-name')} + {request.form.get('last-name')}"
        user = User(name=name, username=request.form.get('username'),
                 password=hashed_password, email=request.form.get('email'))
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created successfully', 'success')
        return redirect(url_for('login'))
    csrf_token = secrets.token_hex(16)
    return render_template('signup.html', csrf_token=csrf_token)


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
    form = UpdateForm()
    image_file = url_for('static', filename='images/profile_pics/' + current_user.image_file)
    return render_template('settings.html', title='NeXa - Account Information', form=form, image_file=image_file)
