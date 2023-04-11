#!/usr/bin/python
import sys
import urllib3

http = urllib3.PoolManager()

url = sys.argv[1]



site = http.request('GET', url)
print (site.status)

