#!/usr/bin/python3
"""

"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import storage
from models.user import User


class RegistrationForm(FlaskForm):
    """

    """
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=50)])
    username = StringField('UserName', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """

        """
        user = storage.filter(User, username.data)
        if user:
            raise ValidationError('Username has already been taken.')

    def validate_email(self, email):
        """

        """
        user = storage.filter(User, email.data)
        if user:
            raise ValidationError('Email has already been taken.')


class LoginForm(FlaskForm):
    """

    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Log in")
