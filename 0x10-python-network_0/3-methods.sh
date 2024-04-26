#!/bin/bash
# cURL only methods
curl -L -sI ALLOW "$1" | grep -i '^Allow:' | cut -d ' ' -f 2-
