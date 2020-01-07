#!/bin/bash
#sends JSON POST request to a URL, and displays the body of the response.
curl -sH POST "Content-Type: application/json" -d @"$2" "$1"
