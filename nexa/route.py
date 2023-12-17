#!/usr/bin/python3
"""

"""


from flask import render_template, flash, redirect, url_for, request
from PIL import Image
from nexa import app
from nexa import db
from nexa import bcrypt
from nexa.form import RegistrationForm, LoginForm, UpdateForm, PostForm
from nexa.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os


@app.route('/')
@app.route('/about')
def index():
    """
    landing page
    """
    return render_template('index.html')


@login_required
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    home page displayed when a user is logged in
    A user can view, create, edit and delete posts
    """
    form = PostForm()
    if current_user.is_authenticated:
        if request.method == 'POST':
            post = Post(content=form.content.data, user=current_user)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('home'))
        posts = Post.query.order_by(Post.posted_at.desc()).all()
        return render_template('home.html', title='Nexa - Home', form=form, posts=posts)
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
        name = f"{form.first_name.data} {form.last_name.data}"
        user = User(name=name, username=form.username.data,
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
    form = UpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            photo_filename = save_upload_photo(form.picture.data)
            current_user.image_file = photo_filename
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        """db.session.add(current_user)"""
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('settings'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/profile_pics/' + current_user.image_file)
    return render_template('settings.html', title='NeXa - Account Information', form=form, image_file=image_file)


def save_upload_photo(picture):
    """

    """
    hex_random = secrets.token_hex(8)
    _, file_ext = os.path.splitext(picture.filename)
    picture_filename = hex_random + file_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_filename)

    size = (125, 125)
    image = Image.open(picture)
    image.thumbnail(size)
    image.save(picture_path)
    return picture_filename


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """

    """
    if current_user.is_authenticated:
        posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', title='NeXa - Profile', posts=posts)
