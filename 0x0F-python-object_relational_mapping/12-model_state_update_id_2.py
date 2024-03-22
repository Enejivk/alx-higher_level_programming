#!/usr/bin/python3
"""a script that changes the name of a State
object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))
Session = sessionmaker(engine)
session = Session()
update_string = (update(State)
                 .where(State.id == 2)
                 .values(name='New Mexico')
                 )
session.execute(update_string)
session.commit()
session.close()
