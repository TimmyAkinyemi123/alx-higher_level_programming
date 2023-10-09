#!/usr/bin/python3
# 1-my_list.py

""""Defines inherited class MyList"""


class MyList(list):
    """Implements the sorted function"""

    def print_sorted(self):
        """"Prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
