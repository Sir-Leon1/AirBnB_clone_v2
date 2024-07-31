#!/usr/bin/python3
"""Defines the place class."""
from os import getenv

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import Table

from models.review import Review


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

    association_table = Table("place_amenity", Base.metadata,
                              Column("place_id", String(60),
                                     ForeignKey("places.id"),
                                     primary_key=True, nullable=False),
                              Column("amenity_id", String(60),
                                     ForeignKey("amenities.id"),
                                     primary_key=True, nullable=False),
                              mysql_engine="InnoDB",
                              mysql_charset="latin1"
                              )

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False, back_populates="place_amenities")

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'latin1'
    }

    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities"""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.ameinty.ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
