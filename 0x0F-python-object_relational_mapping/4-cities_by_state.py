#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """
# Usage: ./4-cities_by_state.py username password db_name
import sys
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("""SELECT c.id, c.name, s.name FROM cities c INNER JOIN
                   states s ON c.state_id = s.id ORDER BY c.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    con.close()
