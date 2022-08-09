#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, \
                delete-orphan")
    else:
        @property
        def cities(self):
            """cities"""
            from models import storage
            stacit = []
            for state in storage.all(City).values():
                if city.state_id == self.id:
                    stacit.append(models.storage.all(City)[state])
            return stacit
