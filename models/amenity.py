#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Representation of an Amenity"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'amenities'
        amenity_name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary="place_amenity",
                                       cascade="all",
                                       viewonly=False)
    else:
        amenity_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes an Amenity"""
        super().__init__(*args, **kwargs)


