#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base

class Review(BaseModel, Base):
&quot;&quot;&quot;Representation of a Review&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &#39;db&#39;:
__tablename__ = &#39;reviews&#39;
review_place_id = Column(String(60), ForeignKey(&#39;places.id&#39;),
nullable=False)
review_user_id = Column(String(60), ForeignKey(&#39;users.id&#39;),
nullable=False)
review_text = Column(String(1024), nullable=False)
else:
review_place_id = &quot;&quot;
review_user_id = &quot;&quot;
review_text = &quot;&quot;

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes a Review&quot;&quot;&quot;
super().__init__(*args, **kwargs)
