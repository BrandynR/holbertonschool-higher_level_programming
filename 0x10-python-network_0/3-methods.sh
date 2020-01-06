#!/bin/bash
#displays all HTTP methods the server will accept
curl -Is "$@" | grep 'Allow' | cut -d ' ' -f 2-
