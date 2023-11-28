#!/usr/bin/python3
""" Script that adds the State object “Louisiana” """

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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
