#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the databse hbtn_ 0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    try:
        cur.execute("SELECT * FROM `states` WHERE name REGEXP '^N'")
        [print(state) for state in cur.fetchall()]
    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        cur.close()
        db.close()
