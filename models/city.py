from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
import os


class City(BaseModel, Base):
    """ city class """
    type_storage = os.getenv("HBNB_TYPE_STORAGE")
    __tablename__ = "cities"
    
    if type_storage == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False,)
        places = relationship("Place", cascade="all,delete", backref='cities')
    else:
        name = ""
        state_id = ""
