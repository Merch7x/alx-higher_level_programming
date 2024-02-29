#!/bin/bash
#sends a json POST request
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
