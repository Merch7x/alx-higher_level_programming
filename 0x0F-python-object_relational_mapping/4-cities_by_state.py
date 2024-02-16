#!/usr/bin/python3
"""
Lists all cities from the databse hbtn_ 0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: <user> <passwd> <db>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            "SELECT cities.id, cities.name, states.name \
                FROM cities\
                    INNER JOIN states ON states.id = cities.state_id")
        [print(city) for city in cur.fetchall()]
    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        cur.close()
        db.close()
