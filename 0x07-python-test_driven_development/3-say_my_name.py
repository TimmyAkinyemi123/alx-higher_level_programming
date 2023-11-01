#!/usr/bin/python3
"""Module containing a function to print first and last name"""


def say_my_name(first_name, last_name=""):
    """ prints first and last name
        Arguments:
            @first_name: first name to be printed
            @last_name: last_name to be printed
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    full_name = "{} {}".format(first_name, last_name) if
    first_name and last_name else first_name or last_name
    print("My name is {}".format(full_name))
