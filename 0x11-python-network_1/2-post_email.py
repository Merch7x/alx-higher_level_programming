#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
 """
from urllib.request import Request, urlopen
from urllib.error import URLError
from urllib.parse import urlencode
import sys


if __name__ == '__main__':
    value = {'email': sys.argv[2]}
    data = urlencode(value)
    data = data.encode('ascii')
    req = Request(sys.argv[1], data)

    try:
        with urlopen(req) as response:
            content = response.read().decode('utf-8')
            print(content)
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
