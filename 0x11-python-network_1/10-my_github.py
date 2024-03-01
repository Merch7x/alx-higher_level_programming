#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
 """
from requests.auth import HTTPBasicAuth
import sys
import requests


if __name__ == '__main__':
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(
        f'https://api.github.com/users/{sys.argv[1]}', auth=basic)
    data = req.json()
    print(data['id'])
