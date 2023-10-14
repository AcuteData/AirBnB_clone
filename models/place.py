#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if getenv("HBNB_TYPE_STORAGE") == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))

class Place(BaseModel, Base):
    """Representation of a Place"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        place_city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        place_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place_name = Column(String(128), nullable=False)
        place_description = Column(String(1024), nullable=True)
        place_number_rooms = Column(Integer, nullable=False, default=0)
        place_number_bathrooms = Column(Integer, nullable=False, default=0)
        place_max_guest = Column(Integer, nullable=False, default=0)
        place_price_by_night = Column(Integer, nullable=False, default=0)
        place_latitude = Column(Float, nullable=True)
        place_longitude = Column(Float, nullable=True)
        place_reviews = relationship("Review", cascade="all")
        place_amenities = relationship("Amenity", secondary="place_amenity", cascade="all", viewonly=False)
    else:
        place_city_id = ""
        place_user_id = ""
        place_name = ""
        place_description = ""
        place_number_rooms = 0
        place_number_bathrooms = 0
        place_max_guest = 0
        place_price_by_night = 0
        place_latitude = 0.0
        place_longitude = 0.0
        place_amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes a Place"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances"""
            from models.review import Review
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances"""
            from models.amenity import Amenity
            return [amenity for amenity in models.storage.all(Amenity).values() if amenity.place_id == self.id]

