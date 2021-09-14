from urllib import parse
key_word = {'wd': '爬虫'}
result = parse.urlencode(key_word)
baseurl = 'http://www.google.com/s?%s'
print(baseurl % result)