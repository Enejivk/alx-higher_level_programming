#!/bin/bash
# Bash script that return the exact number of the content length
curl -Is "$1" | grep -w 'content-length' | cut -f2 -d' '
