#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
 """
from requests.auth import HTTPBasicAuth
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
