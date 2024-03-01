#!/usr/bin/python3
"""
takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
 """
import requests
import sys


if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data=value)

    try:
        data = req.json()
        if data == {}:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
