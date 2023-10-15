#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Representation of a User"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        user_email = Column(String(128), nullable=False)
        user_password = Column(String(128), nullable=False)
        user_first_name = Column(String(128), nullable=True)
        user_last_name = Column(String(128), nullable=True)
        user_places = relationship("Place", cascade="all")
        user_reviews = relationship("Review", cascade="all")
    else:
        user_email = ""
        user_password = ""
        user_first_name = ""
        user_last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a User"""
        super().__init__(*args, **kwargs)

