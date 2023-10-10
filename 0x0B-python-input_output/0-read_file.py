#!/usr/bin/python3
# 0-read_file

"""Defines a function to read text files"""


def read_file(filename=""):
    """Prints the contents of a text file(UTF8) to stdout
    Args:
        filename (str): file to write to
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
