#!/bin/bash
#sends a json POST request
curl -sX POST -d "$(cat "$2") "$1"
