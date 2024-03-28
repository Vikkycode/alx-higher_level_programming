#!/usr/bin/python3
""" send a request to the URL and displays the value of the X-request-id"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    Req = urllib.request.Request(url)

    with urllib.request.urlopen(Req) as response:
        print(dict(response.headers).get("X-Request-Id"))
