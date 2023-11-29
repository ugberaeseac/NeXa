#!/usr/bin/python3
"""

"""


from flask import render_template, flash, redirect, url_for
from flask_app import app, bcrypt
from flask_app.form import RegistrationForm, LoginForm
from models.user import User
from models import storage


@app.route('/')
def index():
    """

    """
    return 'index.html'

@app.route('/home')
def home():
    """

    """
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """

    """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(
                    form.username.data).decode('utf-8')
        user = User(name=form.name.data, username=form.username.data,
                    password=hashed_pwd, email=form.email.data)
        storage.add(user)
        storage.save()
        flash('Your account has been created successfully', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """

    """
    form = LoginForm()
    if form.validate_on_submit():

        flash('Login successful', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)
