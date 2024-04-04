#!/bin/bash
# send a GET request to a URL with curl, with a custom header variable
curl -sI -H "X-School-User-Id: 98" "$1"
