import urllib.request
response = urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
print(html)

# we can find "user-agent" shows we use python-spider to visit website

