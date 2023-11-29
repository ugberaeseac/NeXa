#!/usr/bin/python3
"""

"""


from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is a temp key'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from flask_app import route
