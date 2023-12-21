#!/usr/bin/python3
"""
Forms for user input
    - Registration form
    - Login form
    - Update form
    - Post form
    - Delete form
"""


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from nexa.models import User


class RegistrationForm(FlaskForm):
    """
    Registration form
    """
    first_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    username = StringField('UserName', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """
        custom user validation
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username has already been taken.')

    def validate_email(self, email):
        """
        custom email validation
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email has already been taken.')


class LoginForm(FlaskForm):
    """
    Login form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log in")


class UpdateForm(FlaskForm):
    """
    Update account form
    """
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=50)])
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Upload Photo', validators=[FileAllowed(['jpg', 'jpeg', 'bmp', 'png', 'svg'])])
    save = SubmitField('Save')

    def validate_username(self, username):
        """
        custom user validation
        """
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username has already been taken.')

    def validate_email(self, email):
        """
        custom email validation
        """
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email has already been taken.')


class PostForm(FlaskForm):
    """
    form to create posts
    """
    content = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')


class DeleteForm(FlaskForm):
    """
    Delete an account form
    """
    full_name = StringField('Name', validators=[DataRequired(), Length(min=4, max=50)])
    delete = SubmitField('Delete this account')
