#!/usr/bin/python3
"""

"""

import models
from models.base import Base
from datetime import datetime
import sqlalchemy
from sqlalchemy import Integer, Column, String, ForeignKey, Text, DateTime


class Comment(Base):
    """

    """
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """

        """
        msg = 'Comment({}, {}, {}'
        return msg.format(self.id, self.comment, self.created_at)
