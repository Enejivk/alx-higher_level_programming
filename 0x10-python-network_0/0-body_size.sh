#!/bin/bash
# Bash script that return the exact number of the content length
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
