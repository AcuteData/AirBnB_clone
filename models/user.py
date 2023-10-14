#!/usr/bin/python

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
&quot;&quot;&quot;Representation of a User&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &#39;db&#39;:
__tablename__ = &#39;users&#39;
user_email = Column(String(128), nullable=False)
user_password = Column(String(128), nullable=False)
user_first_name = Column(String(128), nullable=True)
user_last_name = Column(String(128), nullable=True)
user_places = relationship(&quot;Place&quot;, cascade=&quot;all&quot;)
user_reviews = relationship(&quot;Review&quot;, cascade=&quot;all&quot;)
else:
user_email = &quot;&quot;
user_password = &quot;&quot;
user_first_name = &quot;&quot;
user_last_name = &quot;&quot;

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes a User&quot;&quot;&quot;
super().__init__(*args, **kwargs)
