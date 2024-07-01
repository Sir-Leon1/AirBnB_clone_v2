#!/usr/bin/python3
"""Defines the review class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represent a review.

    Attributes:
    place_id (str): The place id
    user_id (str): The user id
    text (str): The text of the review
    """

    __tablename__ = 'reviews'

    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
    user = relationship('User', back_populates='reviews')

