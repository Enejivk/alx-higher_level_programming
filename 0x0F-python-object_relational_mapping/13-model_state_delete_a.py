#!/usr/bin/python3
"""Deleting every state that has the character 'a' """

from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]), echo=True)

    Session = sessionmaker(engine)
    session = Session()
    deleteString = (delete(State)
                    .where(State.name.ilike('%a%')))

    session.execute(deleteString)
    session.commit()
    session.close()
