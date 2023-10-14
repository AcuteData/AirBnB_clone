#!/usr/bin/python3

from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
    """Representation of a State"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        state_name = Column(String(128), nullable=False)
        state_cities = relationship("City", cascade="all")
    else:
        state_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a State"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter for a list of City instances related to the state"""
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

