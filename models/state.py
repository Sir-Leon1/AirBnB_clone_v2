#!/usr/bin/python3
"""Defines the state class."""
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """Represent a state.

    Attributes:
    name (str): The name of the state
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'latin1'
    }

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
