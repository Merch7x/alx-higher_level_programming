#!/bin/bash
#sends a json POST request
curl -sX POST -d "@$2" "$1"
