#!/bin/bash
# This script responds with "You hot me!"
curl -sLX PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool
