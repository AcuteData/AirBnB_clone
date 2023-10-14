#!/usr/bin/python
&quot;&quot;&quot; holds class City&quot;&quot;&quot;
from os import getenv
from sqlalchemy import Column, String, ForeignKey

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class City(BaseModel, Base):
&quot;&quot;&quot;Representation of a City&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &quot;db&quot;:
__tablename__ = &#39;cities&#39;
city_state_id = Column(String(60), ForeignKey(&#39;states.id&#39;),
nullable=False)
city_name = Column(String(128), nullable=False)
city_places = relationship(&quot;Place&quot;, cascade=&quot;all&quot;)
else:
city_state_id = &quot;&quot;
city_name = &quot;&quot;

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes a City&quot;&quot;&quot;
super().__init__(*args, **kwargs)
