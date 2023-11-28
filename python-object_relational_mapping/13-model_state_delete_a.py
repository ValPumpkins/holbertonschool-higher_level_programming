#!/usr/bin/python3
""" Script that deletes all State objects with a name containing the letter a """

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

    query = session.query(State).filter(State.name.like(
        "%a%")).delete(synchronize_session="fetch")

    session.commit()

    session.close()
