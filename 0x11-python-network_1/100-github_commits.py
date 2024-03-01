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

    for commit in data[:10]:
        print(f"{commit.get('sha')}: {commit.get('commit')['author']['name']}")
