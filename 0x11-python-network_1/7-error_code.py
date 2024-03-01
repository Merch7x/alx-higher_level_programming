#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
 """
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    status = req.status_code
    if status >= 400:
        print(f'Error code: {status}')
    else:
        print(req.text)
