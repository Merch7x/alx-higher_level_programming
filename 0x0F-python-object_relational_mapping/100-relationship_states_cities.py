#!/usr/bin/python3
"""hat prints all City objects from the database
"""
import sys
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state_obj = State(name='California')
        new_city_obj = City(name='San Francisco')
        new_state_obj.cities.append(new_city_obj)
        session.add(new_state_obj)
        session.commit()
