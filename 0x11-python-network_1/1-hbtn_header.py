#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
 """
from urllib.request import Request, urlopen
from urllib.error import URLError
import sys


if __name__ == '__main__':
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            content = response.headers.get('X-Request-Id')
            print(content)
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
