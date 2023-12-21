#!/usr/bin/python3
"""
contains the User, Post and Comment class
maps tables to python object
print official representation of the classes
"""


from datetime import datetime
from nexa import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """
    Loads a user from the database by the user id
    """
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    create a User class which represents the users table
    in the database
    Map users table to python object
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='image.jpg')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    posts = db.relationship('Post', backref='user',
                         cascade='all, delete, delete-orphan')
    comments = db.relationship('Comment', backref='user',
                            cascade='all, delete, delete-orphan')

    def __repr__(self):
        """
        Prints official string representation of the User class
        """
        msg = "User({}, {}, {}, {}, {})"
        return msg.format(self.username, self.name, self.email,
                          self.created_at, self.image_file)



class Post(db.Model):
    """
    create a Post class which represents the posts table
    in the database
    Maps the posts table to python object
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    posted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.relationship('Comment', cascade='all, delete, delete-orphan',
                            backref='post')

    def __repr__(self):
        """
        Prints official string representation of the Post class
        """
        msg = 'Post({}, {}, {})'
        return msg.format(self.id, self.content, self.posted_at)



class Comment(db.Model):
    """
    create a Comment class which represents the comments table
    in the database
    Maps the comments table to python object
    """
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """
        Prints official string representation of the Comment class
        """
        msg = 'Comment({}, {}, {}'
        return msg.format(self.id, self.comment, self.created_at)
