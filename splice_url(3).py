from urllib import parse
baseurl = 'http://www.google.com/s?{}'
key_word = input('Please input the content you wanna search: ')
word = {'wd': key_word}
encoding = parse.urlencode(word)
result = baseurl.format(encoding)
print(result)