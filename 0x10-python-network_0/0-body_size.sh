#!/bin/bash
# Bash script that return
curl -Is "$1" | grep -w 'content-length' | cut -f2 -d' '
