#!/bin/bash
# Response status code output
curl -o /dev/null -sw "%{http_code}" "$1"
