#!/usr/bin/python3
""" it takes in a url and an email send a post request"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url = sys.argv[1]
    value = {"Your email is": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
