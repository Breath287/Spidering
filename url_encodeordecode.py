# urlencode()
from urllib import parse
# create query of dictionary with key word
query_str = {'wd': '爬虫'}

# call parse module to encode
result = parse.urlencode(query_str)

# use format function to format string and splice the url
url = 'http://www.google.com/s?{}'.format(result)
print(url)




