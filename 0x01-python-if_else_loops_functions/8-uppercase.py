#!/bin/python3
def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False

def uppercase(str):
    for c in str:
        print(f"{ord(c)}" if not islower(c) else ord(c) - 3        2), end="")
        print("")
