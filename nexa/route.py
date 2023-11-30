#!/usr/bin/python3
"""

"""


from flask import render_template, flash, redirect, url_for
from nexa import app
from nexa import db
from nexa import bcrypt
from nexa.form import RegistrationForm, LoginForm
from nexa.models import User, Post, Comment


@app.route('/')
def index():
    """

    """
    return render_template('index.html')

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
