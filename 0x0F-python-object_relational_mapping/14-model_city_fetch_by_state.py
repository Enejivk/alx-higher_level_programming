#!/usr/bin/python3
"""inner join in sqlalchemy"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(engine)
    session = Session()
    result = session.query(State.name, City.id, City.name)\
                    .join(City, State.id == City.state_id).all()
    for row in result:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))
