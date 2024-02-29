#/bin/bash
#print out only a status code
curl -sw %{http_code} -o /dev/null "$1"
