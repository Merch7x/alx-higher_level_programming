#!/usr/bin/python3
"""Fetchs a status from a url"""
from urllib.request import Request, urlopen
from urllib.error import URLError


if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')

    try:
        with urlopen(req) as response:
            content = response.read()
            body = f"""Body response:
            - type: {type(content)}
            - content: {content}
            - utf8 content: {content.decode("utf-8")}"""
            print(body)
    except URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
