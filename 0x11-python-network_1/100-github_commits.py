#!/usr/bin/python3
"""
This script connects the github api and fetches commits
from a specified repository
its prints out the sha of the commit and the commiters name
"""
import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    try:
        req = requests.get(url)
        req.raise_for_status()  # Raise an HTTPError for bad responses

        data = req.json()

        for x in range(min(10, len(data))):
            commit = data[x]
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))

    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
    except IndexError:
        print("Less than 10 commits available.")
