#!/usr/bin/python3

"""Script that adds all arguments to a Python list
and saves them to a JSON file."""

import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

json_file = "add_item.json"

if os.path.exists(json_file):
    my_list = load_from_json_file(json_file)
else:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, json_file)

print(my_list)
