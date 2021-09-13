# coding=gbk
from urllib import request
import re
import time
import random
from ua_info2 import ua_list
import pymysql


class MaoyanSpider(object):
    def __init__(self):
        # initialize url
        self.url = 'https://maoyan.com/board/4?offset={}'
        # initialize mysql
        self.db = pymysql.connect(host='localhost', user='root', password='lijie1229', db='maoyandb', charset='utf8')
        # initialize cursor
        self.cursor = self.db.cursor()

    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        # call parse function
        self.parse_html(html)

    def parse_html(self, html):
        # regex
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    def save_html(self, r_list):
        L = []
        sql = 'insert into movieinfo values(%s,%s,%s)'
        # data management
        for r in r_list:
            t = (
                r[0].strip(),
                r[1].strip()[3:],
                r[2].strip()[5:15]
            )
            L.append(t)
            print(L)
        # insert multiple lines at a time
        try:
            self.cursor.executemany(sql, L)
            # submit data
            self.db.commit()
        except:
            # rollback once errors
            self.db.rollback()

    def run(self):
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1, 3))
        # close connection between cursor and maoyandb
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.run()
    end = time.time()
    print("执行时间:%.2f" % (end-start))