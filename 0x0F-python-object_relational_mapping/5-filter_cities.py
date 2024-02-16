#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state
"""
import sys
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: <user> <passwd> <db> <state_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()
        cur.execute(
            "SELECT cities.name\
                FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                        WHERE states.name = '{}'".format(sys.argv[4]))
        rows = cur.fetchall()
        frows = []

        for row in rows:
            frows.append(", ".join(map(str, row)))

        print(", ".join(frows))
    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        cur.close()
        db.close()
