import re
from urllib import request
import time
import csv
import random
from ua_info2 import ua_list


""" use python spidering maoyan top 10 movies
including name, release time, starring actors and so on """


""" 1. webpage is static by checking source codes
    2. summarize the pages url pattern, start at offset = 0, then 10, 20
       so we can get parameters offset in a pattern offset = (n - 1)*10
    3. check element structure for writing regex 
       <div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>
"""

# define a spider class of maoyan


class MaoyanSpider:
    # initialize url
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

    # request function
    def get_html(self, url):
        headers = {'User-Agent': random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        self.parse_html(html)

    # parse function
    def parse_html(self, html):
        # regex
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>'
        # generate re object
        pattern = re.compile(re_bds, re.S)
        # generate list
        r_list = pattern.findall(html)
        self.save_html(r_list)

    # save function
    def save_html(self, r_list):
        with open('maoyan.csv', 'a', newline='', encoding="utf-8") as f:
            # generate csv file
            writer = csv.writer(f)
            for r in r_list:
                name = r[0].strip()
                star = r[1].strip()[3:]
                leasetime = r[2].strip()[5:15]
                lis = [name, star, leasetime]
                writer.writerow(lis)
                print(name, leasetime, star)

    # main function
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
        print('Someting wrong: ', e)
