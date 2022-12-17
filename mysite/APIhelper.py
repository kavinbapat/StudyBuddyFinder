import urllib.request


# I used the python documentation to learn how to use this library
# URL: https://docs.python.org/3/library/urllib.request.html#module-urllib.request
# License: Zero Clause BSD license
# Title: urllib.request — Extensible library for opening URLs
# Author: Python Foundation
def callAPI(APIurl):
    info = urllib.request.urlopen(APIurl, data=None)
    print(info.getcode())
    return info.read()


x = callAPI("http://luthers-list.herokuapp.com/api/dept/CS/?format=json")
print(x);
