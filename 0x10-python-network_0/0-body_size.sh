#!/bin/bash
# Usage: ./0-body_size.sh 0.0.0.0:5000L>
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
