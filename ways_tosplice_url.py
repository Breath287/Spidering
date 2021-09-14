from urllib import parse

string = '爬虫'
baseurl = 'http://www.google.com/s?'
result = parse.quote(string)
print(baseurl+result)