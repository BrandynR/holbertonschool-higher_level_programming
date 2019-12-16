#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    for city, state in session.query(City, State)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id.asc()).all():
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()
