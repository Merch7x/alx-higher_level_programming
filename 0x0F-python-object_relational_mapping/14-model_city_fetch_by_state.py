#!/usr/bin/python3
"""hat prints all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        objs = session.query(City, State).join(State).all()

        for _c, _s in objs:
            print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))
