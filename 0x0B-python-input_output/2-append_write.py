#!/usr/bin/python3
# 2-append_write

"""Defines a function that appends to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file
    Args:
       filename (str): name of the file to write to
       text (str): string of characters to write
    Return:
       the number of characters written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
