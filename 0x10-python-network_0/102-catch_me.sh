#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me server responds with a message
curl -sL 0.0.0.0:5000/catch_me -X PUT -d user_id=98 -H "Origin: HolbertonSchool"
