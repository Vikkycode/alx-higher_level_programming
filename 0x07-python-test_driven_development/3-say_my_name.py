#!/usr/bin/python3
# 3-say_my_name.py
 
""" 3 say name function """

def say_my_name(first_name, last_name=""):
    """ say first and last name 

    args:
        first_name(str): first name to print
        last_name(str): last name to print

    """

    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
