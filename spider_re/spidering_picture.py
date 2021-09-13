import re
import requests
from ua_info2 import ua_list
import random

url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1631315156605_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=python+logo'
headers = {'User-Agent': random.choice(ua_list)}
html = requests.get(url=url, headers=headers).text
re_bds = '"thumbURL":"(.*?)",'
pattern = re.compile(re_bds, re.S)
r_list = pattern.findall(html)
for pic in r_list:
    print(pic)


"""
1. requests.request() 
   construct an object
2. requests.get()
   get html
3. requests.head()
   get data in headers
4. requests.post()
   post
5. requests.put()
   put 
6.requests.patch()
  get part change request
7.requests.delete()
  get delete request
"""