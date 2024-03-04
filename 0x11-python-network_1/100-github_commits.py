#!/usr/bin/python3
"""
This script connects the github api and fetches commits
from a specified repository
its prints out the sha of the commit and the commiters name
"""
import sys
import requests

if __name__ == '__main__':
    req = requests.get(
        f'https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits')
    data = req.json()

    try:
        for x in range(10):
            print("{}: {}".format(
                data[x].get('sha'),
                data[x].get('commit').get('author').get('name')))
    except IndexError:
        pass
