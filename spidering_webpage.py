from urllib import request
from urllib import parse


# splice the intact url
url = 'http://www.baidu.com/s?wd={}'
# use quote() to encode
word = input('Input the key words: ')
params = parse.quote(word)
full_url = url.format(params)

# send request to full_url
# refactor the headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/73.0.3683.75 Safari/537.36'}
# generate response
req = request.Request(url=full_url, headers=headers)
# get response
res = request.urlopen(req)
# get html data
html = res.read().decode('utf-8')

filename = word + '.html'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)