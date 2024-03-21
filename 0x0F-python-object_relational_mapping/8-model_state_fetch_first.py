#!/usr/bin/python3
"""script that prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(engine)
    session = Session()
    firstState = session.query(State).order_by(State.id.asc()).first()
    if (firstState):
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")
