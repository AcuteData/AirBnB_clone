#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey,
Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &#39;db&#39;:
place_amenity = Table(&#39;place_amenity&#39;, Base.metadata,

Column(&#39;place_id&#39;, String(60),
ForeignKey(&#39;places.id&#39;,
onupdate=&#39;CASCADE&#39;,
ondelete=&#39;CASCADE&#39;),
primary_key=True),
Column(&#39;amenity_id&#39;, String(60),
ForeignKey(&#39;amenities.id&#39;,
onupdate=&#39;CASCADE&#39;,
ondelete=&#39;CASCADE&#39;),
primary_key=True))

class Place(BaseModel, Base):
&quot;&quot;&quot;Representation of a Place&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &#39;db&#39;:
__tablename__ = &#39;places&#39;
place_city_id = Column(String(60), ForeignKey(&#39;cities.id&#39;),
nullable=False)
place_user_id = Column(String(60), ForeignKey(&#39;users.id&#39;),
nullable=False)
place_name = Column(String(128), nullable=False)
place_description = Column(String(1024), nullable=True)
place_number_rooms = Column(Integer, nullable=False,
default=0)
place_number_bathrooms = Column(Integer, nullable=False,
default=0)
place_max_guest = Column(Integer, nullable=False, default=0)
place_price_by_night = Column(Integer, nullable=False,
default=0)
place_latitude = Column(Float, nullable=True)
place_longitude = Column(Float, nullable=True)
place_reviews = relationship(&quot;Review&quot;, cascade=&quot;all&quot;)
place_amenities = relationship(&quot;Amenity&quot;,
secondary=&quot;place_amenity&quot;, cascade=&quot;all&quot;, viewonly=False)

else:
place_city_id = &quot;&quot;
place_user_id = &quot;&quot;
place_name = &quot;&quot;
place_description = &quot;&quot;
place_number_rooms = 0
place_number_bathrooms = 0
place_max_guest = 0
place_price_by_night = 0
place_latitude = 0.0
place_longitude = 0.0
place_amenity_ids = []

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes a Place&quot;&quot;&quot;
super().__init__(*args, **kwargs)

if getenv(&quot;HBNB_TYPE_STORAGE&quot;) != &#39;db&#39;:
@property
def reviews(self):
&quot;&quot;&quot;Getter attribute that returns the list of Review
instances&quot;&quot;&quot;
from models.review import Review
return [review for review in
models.storage.all(Review).values() if review.place_id == self.id]

@property
def amenities(self):
&quot;&quot;&quot;Getter attribute that returns the list of Amenity
instances&quot;&quot;&quot;
from models.amenity import Amenity

return [amenity for amenity in
models.storage.all(Amenity).values() if amenity.place_id == self.id]
