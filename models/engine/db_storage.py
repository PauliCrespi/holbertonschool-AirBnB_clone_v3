#!/usr/bin/python3
"""Database Storage"""


from models.user import User
from models.base_model import BaseModel, Base
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

class DBStorage:
    """Database"""
    __engine = None
    __session = None

    def __init__(self):
        """inisialization"""
        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}')
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.meta.drop_all(self.__engine)

    def all(self, cls=None):
        """all func"""
        model_ = {"User": User, "State": State,
         "City": City, "Amenity": Amenity,
         "Place": Place, "Review": Review}
        dic = {}
        for c in model_:
            if c == model_[c] or cls is None:
                query = self.__session.query(model_[c]).all()
                for elem in query:
                    key = elem.__class__.__name__ + '.' + elem.id
                    dic[key] = elem
        return dic

    def new(self, obj):
        """new"""
        self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        __session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(__session)
        self.__session = Session
