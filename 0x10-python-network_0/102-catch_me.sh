#!/bin/bash
#makes a request to loclhost on port 5000 respond with a message
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0:5000/catch_me
