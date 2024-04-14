#!/usr/bin/python3
''' module that contains the class definition of a State '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    '''city class

    __tablename__: name of mysql table
    id: id of state
    name: name of state
    state_id = foreign key to states.id
    '''
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
