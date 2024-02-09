#!/usr/bin/python3
"""This defines the module for State class."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state"""
    __tablename__ = 'states'
    id = Column(
            Integer, primary_key=True, nullable=False, unique=True
            )
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
            )
