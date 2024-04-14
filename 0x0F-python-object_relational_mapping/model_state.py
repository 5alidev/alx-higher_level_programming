#!/usr/bin/python3
''' module that contains the class definition of a State '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''state class

    __tablename__: name of mysql table
    id: id of state
    name: name of state
    '''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
