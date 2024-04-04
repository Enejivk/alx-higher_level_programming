#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response. no pipe
curl -sI "$1" -o test7; awk 'NR==1{print $2}' test7; rm test7