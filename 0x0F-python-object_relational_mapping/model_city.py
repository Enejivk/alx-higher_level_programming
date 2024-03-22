#!/usr/bin/python3
"""Creating a city table"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base
from sys import argv

Base = declarative_base()


class City(Base):
    """creating a city table"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'))
