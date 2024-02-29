#!/bin/bash
# gets the body of the http request if the status code is 200
curl -s -X GET "if-Match: \"HTTP/1.1 200 OK\"" $1
