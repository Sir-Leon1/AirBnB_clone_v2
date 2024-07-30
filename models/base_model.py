#!/usr/bin/python3
"""Defines the baseModel class."""
import sys
sys.path.append('/home/sir-leon1/CoDe/Python/alx-higher_level_programming/BnBVenv/lib/python3.10/site-packages')
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String


Base = declarative_base()


class BaseModel:
    """Rep the base model of the hbnh project"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize a new basemodel."""

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Including the key/value pair __class__ rep
        the class name of the object.
        """

        rdict = self.__dict__.copy()
        rdict["__class__"] = str(type(self).__name__)
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict.pop("_sa_instance_state", None)
        return rdict

    def delete(self):
        """Delete current instance from storage"""
        models.storage.delete(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
