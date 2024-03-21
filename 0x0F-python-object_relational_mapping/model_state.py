#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)

    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://secroot:secroot@localhost:\
                           3306/hbtn_0e_6_usa", echo=True)
    Base.metadata.create_all(engine)
