#!/usr/bin/python3
"""Printing all the state and the Id of the state"""

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import sessionmaker
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv

"""Connecting to the database using engine method"""
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(argv[1], argv[2], argv[3]))


    Session = sessionmaker(engine)
    session = Session()
    for id, state in session.query(State.id, State.name).order_by(State.id.asc()):
        print("{}: {}".format(id, state))
