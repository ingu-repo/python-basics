import urllib
import urllib.request 

URL = "http://www.google.com"

req = urllib.request.Request(URL)
with urllib.request.urlopen(req) as res:
    body = res.read()

print (body)


