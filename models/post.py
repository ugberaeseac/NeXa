#!/usr/python3
"""

"""


from datetime import datetime
from models.base import Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship


class Post(Base):
    """

    """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    posted_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    comments = relationship('Comment', cascade='all, delete, delete-orphan',
                            backref='post')

    def __repr__(self):
        """

        """
        msg = 'Post({}, {}, {})'
        return msg.format(self.id, self.content, self.posted_at)
