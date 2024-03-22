#!/usr/bin/python3

"""
Script to list all states from the database hbtn_0e_0_usa.

This script connects to a MySQL server running on localhost at port 3306
and retrieves all states from the database hbtn_0e_0_usa. The results are
sorted in ascending order by states.id and displayed.

Usage: ./list_states.py <username> <password> <database>

Arguments:
    username: MySQL username
    password: MySQL password
    database: MySQL database name

Example:
    ./list_states.py root root hbtn_0e_0_usa
"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
