#!/usr/bin/python3
"""Fetchs a status from a url"""
from urllib.request import Request, urlopen
from urllib.error import URLError


if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')

    try:
        with urlopen(req) as response:
            content = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(content)))
            print("\t- content: {}".format(content))
            print("\t- utf8 content: {}".format(content.decode(encoding='utf-8')))
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
