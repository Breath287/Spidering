# import urllib or you can use 'from urllib import request'
import urllib.request
# use urlopen() send request, then get response, attention that usl must be intact
response = urllib.request.urlopen('http://www.google.com/')
print(response)

# get html information
html = response.read().decode('gbk')
print(html)

code = response.getcode()
print(code)