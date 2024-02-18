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
        for city in session.query(City).order_by(City.id):
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
