from hashlib import md5
from urllib import request
import time
import random
import re
import pymysql
from ua_info2 import ua_list
import sys


"""
check different pages and find the regular pattern
1. the first page: https://dydytt.net/html/gndy/china/list_4_1.html
2. the second page: https://dydytt.net/html/gndy/china/list_4_2.html
3. the third page: https://dydytt.net/html/gndy/china/list_4_3.html
we can find the the patterns with list_4_n(page number)
"""


class MovieSkySpider:
    def __init__(self):
        # initialize url, database and cursor
        self.url = 'https://dydytt.net/html/gndy/china/list_4_{}.html'
        self.db = pymysql.Connect(host='localhost', user='root', password='lijie1229',
                                  db='chinamovieofdytt')
        self.cursor = self.db.cursor()

# 1. request function
    def get_html(self, url):
        # refactor the headers
        headers = {'User-Agent': random.choice(ua_list)}
        # create the request
        req = request.Request(url=url, headers=headers)
        # get response of the request
        res = request.urlopen(req)
        # get the data of response
        html = res.read().decode('gb2312', 'ignore')
        return html

# 2. regex to parse
    def re_func(self, re_bds, html):
        # get re object
        pattern = re.compile(re_bds, re.S)
        # get the list of regex
        r_list = pattern.findall(html)
        return r_list

# 3. extract link data
    def parse_html(self, one_url):
        # send request and get level 1 webpage
        one_html = self.get_html(one_url)
        re_bds = '<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
        # get links of level 2 webpages
        link_list = self.re_func(re_bds, one_html)
        for link in link_list:
            # get fingerprint and splice url of level 2
            two_url = 'https://www.dydytt.net'+link
            secret = md5()
            # encode two_url and get string
            secret.update(two_url.encode())
            # generate fingerprint, and get hexadecimal cipher key
            finger = secret.hexdigest()
            if self.is_hold_on(finger):
                # extract data of level 2 webpages
                self.save_html(two_url)
                time.sleep(random.randint(1, 2))
                # update finger into database request_finger
                ins = 'insert into request_finger values(%s)'
                self.cursor.execute(ins, [finger])
                self.db.commit()
            else:
                sys.exit('Successfully updated!')

# 4. check if link has been extracted
    def is_hold_on(self, finger):
        # inquire database
        sql = 'select finger from request_finger where finger=%s'
        # return value showing if url has been extracted
        r = self.cursor.execute(sql, [finger])
        # if not 0, return True
        if not r:
            return True

# 5. parse level 2 webpages, and extract data
    def save_html(self, two_url):
        two_html = self.get_html(two_url)
        re_bds = '<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1>' \
                 '</div>.*?<a.*?href="(.*?)".*?>.*?style="BACKGROUND-COLOR.*?</a>'
        # get film_list
        film_list = self.re_func(re_bds, two_html)
        print(film_list)
        sql = 'insert into movieinfo values(%s, %s)'
        self.cursor.executemany(sql, film_list)
        self.db.commit()

    def run(self):
        for page in range(1, 4):
            url = self.url.format(page)
            self.parse_html(url)


if __name__ == '__main__':
    spider = MovieSkySpider()
    spider.run()






