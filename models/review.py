#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
    """Representation of a Review"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'reviews'
        review_place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        review_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        review_text = Column(String(1024), nullable=False)
    else:
        review_place_id = ""
        review_user_id = ""
        review_text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a Review"""
        super().__init__(*args, **kwargs)

