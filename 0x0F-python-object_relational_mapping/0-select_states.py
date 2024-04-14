#!/usr/bin/python3
import sys
import MySQLdb
""" script that lists all states from the database hbtn_0e_0_usa """
""" Usage: ./0-select_states.py username password db_name """


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
