#!/usr/bin/bash
# gets the content length of the http request
curl -sI $1 | grep "^Content-Length:" | cut -d ':' -f 2
