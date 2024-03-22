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
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    states = c.fetchall()
    [print(state) for state in states if state[1] == sys.argv[4]]
