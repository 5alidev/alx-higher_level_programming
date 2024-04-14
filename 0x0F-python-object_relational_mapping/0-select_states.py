#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
# Usage: /0-select_states.py username password db_name

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
