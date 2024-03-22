#!/usr/bin/python3
"""Adding new object to the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))
Session = sessionmaker(engine)
session = Session()

newState = State(name='Louisiana')
session.add(newState)
session.commit()
for newState in session.query(State).filter(State.name == 'Louisiana'):
    print(newState.id)
