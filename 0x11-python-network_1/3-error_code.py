#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
 """
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except HTTPError as e:
        print(f'Error code: {e.code}')
