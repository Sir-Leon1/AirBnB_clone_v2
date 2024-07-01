#!/usr/bin/python3
"""Defines the user class."""

from sqlalchemy import Column, String, relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """Rep a user.

    Attributes:
    email (str): The email of the user
    password (str): The password of the user
    first_name (str): The first name of the user
    last_name (str): The last name of the user.
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", back_populates="user", cascade="all, delete-orphan")
