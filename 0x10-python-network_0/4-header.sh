#!/bin/bash
#sends a GET request to URL, displays the body of the response, adds a header
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
