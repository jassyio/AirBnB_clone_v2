#!/usr/bin/python3
""" holds class Place"""
import models
# File: place.py

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Representation of Place"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", cascade="all, delete", backref="places")
    amenities = relationship("Amenity", secondary='place_amenity', viewonly=False, backref="place_amenities")

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute that returns list of Review instances"""
        values_review = models.storage.all("Review").values()
        list_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """attribute that returns list of Amenity instances"""
            values_amenity = models.storage.all("Amenity").values()
            list_amenity = []
            for amenity in values_amenity:
                if amenity.place_id == self.id:
                    list_amenity.append(amenity)
            return list_amenity
