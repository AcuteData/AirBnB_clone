#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
&quot;&quot;&quot;Representation of an Amenity&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &#39;db&#39;:
__tablename__ = &#39;amenities&#39;
amenity_name = Column(String(128), nullable=False)
place_amenities = relationship(&quot;Place&quot;,
secondary=&quot;place_amenity&quot;,
cascade=&quot;all&quot;,
viewonly=False)
else:
amenity_name = &quot;&quot;

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes an Amenity&quot;&quot;&quot;
super().__init__(*args, **kwargs)
