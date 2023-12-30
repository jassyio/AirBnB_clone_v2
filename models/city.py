#!/usr/bin/python3
""" holds class City"""
import models
# File: city.py

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Representation of city"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="cities", cascade="all, delete-orphan")


    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
