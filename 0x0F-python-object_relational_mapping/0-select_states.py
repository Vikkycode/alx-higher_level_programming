#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host=sys.argv[1], user=sys.argv[2], passwd=sys.argv[3], db=sys.argv[4])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY id ASC")
    result = c.fetchall()
    for state in result:
        print(state)
    c.close()
    db.close()
