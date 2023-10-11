#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Interacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST')
        mysql_db = getenv('HBNB_MYSQL_DB')
        hbnb_env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(mysql_user,
                                             mysql_pwd,
                                             mysql_host,
                                             mysql_db))
        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        new_dict = {}
        for class_name in classes:
            if cls is None or cls is classes[class_name] or cls is class_name:
                objs = self.__session.query(classes[class_name]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """Retrieves one object based on the class name and its ID
        Attributes:
            cls (string): string representing the class name
            id (string): string representing the object ID
        Return: the object, or None if not found
        """
        for class_name in classes.keys():
            if cls == class_name:
                objs = self.__session.query(classes[class_name]).all()
                for item in objs:
                    if id == item.id:
                        return item
        return None

    def count(self, cls=None):
        """Returns the number of objects in storage matching the given class
        name. Returns count of all objects in storage if no class name given
        Attributes:
            cls (string): string representing the class name (optional)
        Return: the number of objects in storage
        """
        count = 0
        if cls is not None:
            for class_name in classes.keys():
                if cls == class_name:
                    objs = self.__session.query(classes[class_name]).all()
                    for item in objs:
                        count += 1
        else:
            for class_name in classes.keys():
                objs = self.__session.query(classes[class_name]).all()
                for item in objs:
                    count += 1
        return count
