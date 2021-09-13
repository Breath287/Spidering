from urllib import request
url = 'http://httpbin.org/get'
# refractor the header so that we can visit website by camouflaging the Chrome
headers = {'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/73.0.3683.75 Safari/537.36'}

# create request object, encapsulating UA information
req = request.Request(url=url, headers=headers)

# send request, then get response
res = request.urlopen(req)

# extract response content
html = res.read().decode()
print(html)

# Now, we can find UA shows we use chrome to visit the website
