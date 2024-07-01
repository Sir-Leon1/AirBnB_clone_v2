#!/usr/bin/python3
"""Defines the place class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, relationship


class Place(BaseModel, Base):
    """Represent a place.

    Attributes:
    city_id (str: The city id.
    user_id (str)): The user id
    name (str): The name of the place.
    description (str): DEscription of the place
    number_rooms (int): The number of the rooms of the place
    number_bathrooms (int): Number of bathrooms of the place.
    max_guest (int): The maximum number of guests of the place
    price_by_night (int): The price by night of the place.
    latitude (float): The latitude of the place
    longitude (float): The longitude of the place
    amenity_ids (list): A list of Amenity ids
    """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="place")
    amenity_ids = []
