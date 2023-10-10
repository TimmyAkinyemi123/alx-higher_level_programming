#!/usr/bin/python3

"""Add all arguments to a Python list and save them to a file."""
import sys
from os import path
from importlib import import_module

if not path.isfile("5-save_to_json_file.py") or not path.isfile("6-load_from_json_file.py"):
    raise ImportError(
        "5-save_to_json_file.py and 6-load_from_json_file.py are required."
    )

save_to_json_file = import_module("5-save_to_json_file").save_to_json_file
load_from_json_file = import_module("6-load_from_json_file").load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
