#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list == search:
            new_list = replace
        return (new_list)
