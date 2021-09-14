from urllib import parse
# writing url is different from what you write in urlencode() way
url = 'http://www.google.com/s?wd={}'
key_word = input('Please input content you wanna search: ')

# quote() only can be used to encode string
query_string = parse.quote(key_word)
print(url.format(query_string))
