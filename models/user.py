#!/usr/bin/python3
"""
contains the User class
maps user table to python object
print official representation of the class User
"""


from datetime import datetime
from models.base import Base
from models.post import Post
from models.comment import Comment
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    """
    create a user class which represents the user table
    in the database
    Map relational database tables to python objects
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default='image.jpg')
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    posts = relationship("Post", backref='user',
                         cascade='all, delete, delete-orphan')
    comments = relationship('Comment', backref='user',
                            cascade='all, delete, delete-orphan')

    def __repr__(self):
        """
        Prints official string representation of the user class
        """
        msg = "User({}, {}, {}, {}, {})"
        return msg.format(self.username, self.name, self.email,
                          self.created_at, self.image_file)
