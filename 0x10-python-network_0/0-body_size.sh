#!/bin/bash
# cURL body size
curl -w "%{size_download}\n" -o /dev/null -s "$1"
