#!/usr/bin/python
""" Creates a class State"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+mysqldb://tim:tim@localhost/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """Creates a State object
      Inherits from the Base of sqlalchemy
       """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
