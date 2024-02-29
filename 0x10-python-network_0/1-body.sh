#!/bin/bash
# gets the body of the http request if the status code is 200
curl -s $1 | head -n 1 
