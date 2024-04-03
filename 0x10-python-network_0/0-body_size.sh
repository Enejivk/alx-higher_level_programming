#!/bin/bash
# Bash script that return the exact number of the content length
curl -Is "$1" | grep -w 'Content-length' | cut -f2 -d' '