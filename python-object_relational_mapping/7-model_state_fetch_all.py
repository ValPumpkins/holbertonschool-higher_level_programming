#!/usr/bin/python3
""" Script that lists all State obj """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.format(
        mysql_username,
        mysql_password,
        database_name
        ), pool_pre_ping=True)

    Base = Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    session.close()

    for state in query:
        print("{}: {}".format(state.id, state.name))
