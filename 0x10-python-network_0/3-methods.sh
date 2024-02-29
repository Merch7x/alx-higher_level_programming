#!/bin/bash
# Gets all methods accepted by the server
curl -s -X OPTIONS "$1"
