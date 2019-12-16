#!/usr/bin/python3
"""
Improved model_city.py and model_state.py
"""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class of City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state = Column(Integer, ForeignKey('states.id'))
