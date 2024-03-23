#!/usr/bin/python3
"""
Script that adds a new State with
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create an engine to interact with the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables defined in Base's subclasses
    Base.metadata.create_all(engine)

    # Create a session to perform database operations
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a new City and State to the database
    session.add(City(name="San Francisco", state=State(name="California")))
