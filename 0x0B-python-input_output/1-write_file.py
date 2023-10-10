#!/usr/bin/python3
#1-write_file

"""Defines a function to write to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file
    Args:
       filename (str): name of the file to write to
       text (str): string of characters to write
    Return:
       the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
       return f.write(text)