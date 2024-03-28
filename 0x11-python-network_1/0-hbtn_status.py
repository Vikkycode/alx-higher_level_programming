#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":

    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

    with urllib.request.urlopen(request) as response:
    res = response.read()
    print("Body response:")
    print("\t - type: {}".format(type(res)))
    print("\t - content: {}".format(res))
    print("\t - utf8 content: {}".format(res.decode('utf8')))
