import requests

"""
url = "http://www.google.com"
res = requests.get(url)
print(res)
"""

"""
data = {
    'name': '编程帮',
    'url': "www.biancheng.net"
}

res = requests.get('http://httpbin.org/get', params=data)
print(res.text）
"""

"""
url = 'https://fanyi.baidu.com'
data = {'from': 'zh',
        'to': 'en',
        'query': '编程帮www.biancheng.net你好'
        }
response = requests.post(url, data=data)
print(response)
"""

"""
response = requests.get('http://www.baidu.com')
print(response.encoding)
response.encoding = "utf-8"    # change to utf-8
print(response.status_code)  # get status
print(response.url)          # get url
print(response.headers)      # get headers
print(response.cookies)      # get cookies
print(response.text)         # get source codes in text
print(response.content)      # get source codes in bits
"""

url = 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=38785274,1357847304&fm=26&gp=0.jpg'
# define headers in a simple format
headers = {'User-Agent':'Mozilla/4.0'}
# use content function to get images
html = requests.get(url=url,headers=headers).content
#
with open('/Users/jieli/Desktop/python_logo.jpg', 'wb') as f:
    f.write(html)








