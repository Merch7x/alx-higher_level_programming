#!/bin/bash
# gets the body of the http request if the status code is 200
url=$1

# Send a GET request using curl and capture the response
response=$(curl -s -w "%{http_code}" "$url")

# Extract the status code and response body
status_code=${response:(-3)}  # Extract last 3 characters (status code)
response_body=${response::-3}  # Remove last 3 characters (status code)

# Check if the status code is 200
if [ "$status_code" == "200" ]; then
    echo "$response_body"
else
	exit 1
fi

