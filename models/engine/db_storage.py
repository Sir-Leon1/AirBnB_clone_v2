#!/usr/bin/python3

"""Defines the DB storage engine class."""
from os import getenv
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationships, sessionmaker, scoped_session


class DBStorage:
    """Represents a database storage engine.

    Attributes:
            __engine (SqlAlchemy): the database engine.
            __session (sqlalchemy.orm.scoped_session): the database session
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initializes the database storage instance."""
        self.__engine = create_engine("")
