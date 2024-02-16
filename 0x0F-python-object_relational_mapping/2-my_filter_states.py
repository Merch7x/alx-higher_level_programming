#!/usr/bin/python3
"""
Lists all states with a name provided by the user through cmd input
from the databse hbtn_ 0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: <user> <passwd> <db> <search_parameter>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM `states` where name = '{}'".format(sys.argv[4]))
        [print(state) for state in cur.fetchall()]
    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        cur.close()
        db.close()
