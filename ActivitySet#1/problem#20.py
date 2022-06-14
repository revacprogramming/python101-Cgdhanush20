import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter url-')
data=urllib.request.urlopen(url,context=ctx).read()
info = json.loads(data)

sum=0
count=0

for i in info['comments']:
    sum=sum+int(i['count'])
    count=count+1

print('sum=',sum,'/ncount=',count)