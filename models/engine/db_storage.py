#!/usr/bin/python3
"""

"""


import models
from models.base import Base
from models.post import Post
from models.user import User
from models.comment import Comment
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import re


class DBStorage:
    """

    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Instantiate a database
        """
        NEXA_MYSQL_HOST = getenv('NEXA_MYSQL_HOST')
        NEXA_MYSQL_DB = getenv('NEXA_MYSQL_DB')
        NEXA_MYSQL_USER = getenv('NEXA_MYSQL_USER')
        NEXA_MYSQL_PWD = getenv('NEXA_MYSQL_PWD')
        NEXA_MYSQL_ENV = getenv('NEXA_MYSQL_ENV')

        db_conn = 'mysql+mysqldb://{}:{}@{}/{}'

        self.__engine = create_engine(db_conn.format(
                                                NEXA_MYSQL_USER,
                                                NEXA_MYSQL_PWD,
                                                NEXA_MYSQL_HOST,
                                                NEXA_MYSQL_DB))
        if NEXA_MYSQL_ENV == 'drop':
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)
            sess_factory = sessionmaker(bind=self.__engine,
                                        expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session

    def add(self, obj):
        """

        """
        self.__session.add(obj)

    def save(self):
        """

        """
        self.__session.commit()

    def delete(self, obj=None):
        """

        """
        if obj is not None:
            self.__session.delete(obj)

    def filter(self, cls, data):
        """

        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, data)):
            query = self.__session.query(cls).filter(cls.email == data).first()
        else:
            query = self.__session.query(cls).filter(cls.username == data).first()
        return query

    def all(self, cls):
        """

        """
        query = self.__session.query(cls).all()
        return query

    def get(self, cls, user_id):
        """
        returns object that matches the user id
        """
        query = self.__session.get(cls, user_id)
        return query
