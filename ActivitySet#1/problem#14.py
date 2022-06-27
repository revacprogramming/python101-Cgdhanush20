import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Enter-')
xml=urllib.request.urlopen(url,context=ctx).read()
tree=ET.fromstring(xml)
counts=tree.findall('comments/comment')
sum=0
count=0
for n in counts:
    t=n.find('count').text
    sum=sum+int(t)
    count=count+1
print('sum=',sum,'count=',count)
