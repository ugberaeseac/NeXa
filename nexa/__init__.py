#!/usr/bin/python3
"""

"""


from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


NEXA_MYSQL_HOST = getenv('NEXA_MYSQL_HOST')
NEXA_MYSQL_DB = getenv('NEXA_MYSQL_DB')
NEXA_MYSQL_USER = getenv('NEXA_MYSQL_USER')
NEXA_MYSQL_PWD = getenv('NEXA_MYSQL_PWD')
NEXA_MYSQL_ENV = getenv('NEXA_MYSQL_ENV')

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{NEXA_MYSQL_USER}:{NEXA_MYSQL_PWD}@{NEXA_MYSQL_HOST}/{NEXA_MYSQL_DB}'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from nexa import route


app.app_context().push()
