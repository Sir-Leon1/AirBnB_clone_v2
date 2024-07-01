#!/usr/bin/pythton3
"""Defines the City class."""

from sqlalchemy import ForeignKey, Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Represent a city.

    state_id (str): The state id
    name (str): The name of the city
    """

    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
    places = relationship("Place", back_populates="citiesls", cascade="all, delete-orphan")
