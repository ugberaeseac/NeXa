#!/usr/bin/env python3
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email
from datetime import datetime

# Create Flask instance
app = Flask(__name__)

#Setup CSRF key to be changed later and make more secure
app.config["SECRET_KEY"] = "This is a temp key"

# Index Route
@app.route("/")
def index():
    return render_template("index.html")

# Define Signup form
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("UserName", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    re_password = PasswordField("Retype-Password", validators=[DataRequired()])
    submit = SubmitField("Signup")

# Create signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    name = None
    email = None
    username = None
    password = None
    re_password = None
    form = UserForm()

    # Validate
    if form.validate_on_submit():
        """
        Need to verify <email> and <username> are not used by other users
        If both don't already exist add the data to the db
        """
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        re_password = form.re_password.data
        
        #Reset Fields
        form.name.data = ""
        form.email.data = ""
        form.username.data = ""
        form.password.data = ""
        form.re_password.data = ""
        flash("Signed up successfully")
    return render_template("signup.html",
                           name=name,
                           email=email,
                           username=username,
                           password=password,
                           re_password=re_password,
                           form=form
                           )

#Define Login form
class LoginForm(FlaskForm):
    email_or_username = StringField("Email/Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

# Create login route
@app.route("/login", methods=["GET", "POST"])
def login():
    username = None
    password = None
    form = LoginForm()

    # Validate
    if form.validate_on_submit():
        """
        Need to verify <email> or <username> exist in the database
        """
        
        # Query db for user's Username
        # Replace form.email_or_username.data with {db_query for username if email was entered}
        username = form.email_or_username.data
        password = form.password.data

        #Reset Fields
        form.email_or_username.data = ""
        form.password.data = ""
        flash("Login successful")
    return render_template("login.html",
                           username=username,
                           password=password,
                           form=form
                           )



if __name__ == "__main__":
    app.run(debug=True)