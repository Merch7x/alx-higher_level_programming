#!/usr/bin/python3
"""Defines a database model City"""

from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
from model_state import Base
import sys


class City(Base):
    """Creates city objects 
      Superclass is sqlalchemy's base class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,
                unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # state = relationship('State')

    # def __repr__(self):
    #     return "<state name>: (<city id>) <city name>"\
    #         .format(self.state.name, self.id, self.name)
