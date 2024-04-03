#!/bin/bash
#return a body if it contain 200
if [ $(curl -Is "$1"| grep -w 'HTTP/1.1' | cut -f2 -d' ') = "200" ]; then curl -s "$1"; fi