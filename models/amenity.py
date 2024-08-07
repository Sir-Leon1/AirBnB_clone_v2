#!/usr/bin/python3
"""Defines the amenity class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represent an amenity."""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'latin1'
    }

