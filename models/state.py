
m os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City

class State(BaseModel, Base):
&quot;&quot;&quot;Representation of a State&quot;&quot;&quot;
if getenv(&quot;HBNB_TYPE_STORAGE&quot;) == &quot;db&quot;:
__tablename__ = &#39;states&#39;
state_name = Column(String(128), nullable=False)
state_cities = relationship(&quot;City&quot;, cascade=&quot;all&quot;)
else:
state_name = &quot;&quot;

def __init__(self, *args, **kwargs):
&quot;&quot;&quot;Initializes a State&quot;&quot;&quot;
super().__init__(*args, **kwargs)

if getenv(&quot;HBNB_TYPE_STORAGE&quot;) != &quot;db&quot;:
@property
def cities(self):
&quot;&quot;&quot;Getter for a list of City instances related to the
state&quot;&quot;&quot;
return [city for city in models.storage.all(City).values()
if city.state_id == self.id]
