#!/bin/bash
#sends a POST request to the URL and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
