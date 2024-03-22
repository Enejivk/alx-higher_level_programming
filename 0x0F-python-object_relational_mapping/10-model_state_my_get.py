#!/usr/bin/python3
"""List all the state that contain a"""

from sqlalchemy import create_engine
from model_state import State, Base
from sqlalchemy.orm import declarative_base, sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()
    search_string = '%' + argv[4] + '%'
    part = session.query(State).filter(State.name.ilike(search_string)).all()
    if part:
        for value in part:
            print('{}: {}'.format(value.id, value.name))
    else:
        print("Not found")
