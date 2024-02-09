#!/usr/bin/python3
"""This defines the module for City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    City class inherits from Base.
    Represents a city.
    """
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True, nullable=False, unique=True
            )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(
        'states.id'), nullable=False)
