#!/usr/bin/python3
""" Class definition of a City """

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb


class City(Base):
    """ City class """

    __tablename__ = "cities"

    id = Column(
        Integer,
        unique=True,
        nullable=False,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306
    )
