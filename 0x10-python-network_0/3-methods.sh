#!/bin/bash
# Displays http methods
curl -sI "$1" | grep "Allow:" | cut -d ':' -f 2- | cut -c 2-
