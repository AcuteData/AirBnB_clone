#!/usr/bin/python
""" holds class City"""
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
    """Representation of a City"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        city_state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        city_name = Column(String(128), nullable=False)
        city_places = relationship("Place", cascade="all")
    else:
        city_state_id = ""
        city_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a City"""
        super().__init__(*args, **kwargs)
