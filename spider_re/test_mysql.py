import re
from urllib import request
from ua_info2 import ua_list
import random
import time
import csv


class MaoyanSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        self.parse_html(html)

    def parse_html(self, html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        r_list = pattern.findall(html)
        self.save_html(r_list)

    def save_html(self, r_list):
        with open('maoyan2.csv', 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                time = r[2].strip()[5:15]
                l = [name, star, time]
                writer.writerow(l)
                print(name, time, star)

    def run(self):
        for offset in range(0, 11, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    try:
        spider = MaoyanSpider()
        spider.run()
    except Exception as e:
        print("wrong!", e)




