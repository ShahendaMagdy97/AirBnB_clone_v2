#!/usr/bin/python3
"""This module defines a db_storge class"""
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.place import Place, place_amenity
from models.state import State
from models.review import Review
from models.city import City
from models.user import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


__classes = {"State": State, "Amenity": Amenity,
             "City": City, "Place": Place,
             "Review": Review, "User": User}


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instatntiates a new model"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                                 getenv('HBNB_MYSQL_PWD'),
                                                 getenv('HBNB_MYSQL_HOST'),
                                                 getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querey the current database"""
        io_dictto = {}
        if cls is None:
            class_names = list(__classes.keys())
            g = 0
            while g < len(class_names):
                etn = __classes[class_names[g]]
                objs = self.__session.query(etn).all()
                j = 0
                while j < len(objs):
                    obj = objs[j]
                    key = obj.__class__.__name__ + '.' + obj.id
                    io_dictto[key] = obj
                    j += 1
                g += 1
        else:
            objs = self.__session.query(cls).all()
            g = 0
            while g < len(objs):
                obj = objs[g]
                key = obj.__class__.__name__ + '.' + obj.id
                io_dictto[key] = obj
                g += 1
        return io_dictto

    def new(self, obj):
        """add the object to the current database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """relod from db"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import BaseModel, Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
