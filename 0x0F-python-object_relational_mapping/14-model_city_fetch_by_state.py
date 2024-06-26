#!/usr/bin/python3
''' script that adds the State object “Louisiana” '''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q_rows = session.query(City, State) \
                    .filter(City.state_id == State.id).all()
    for city, state in q_rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
