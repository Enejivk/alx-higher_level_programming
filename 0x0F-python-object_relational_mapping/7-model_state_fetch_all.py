#!/usr/bin/python3
"""Printing all the state and the Id of the state"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import sessionmaker
from model_state import State
from sys import argv


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))


Session = sessionmaker(engine)
session = Session()
for id, state in session.query(State.id, State.name):
    print("{}: {}".format(id, state))
