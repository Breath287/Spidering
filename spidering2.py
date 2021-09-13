from urllib import request, parse
import time
import random
from ua_info import ua_list


# define a spider class
class TiebaSpider:
    # initialize url
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?{}'

    # send request, get response
    def get_html(self, url):
        req = request.Request(url=url, headers={'User-Agent': random.choice(ua_list)})
        res = request.urlopen(req)
        # in windows, there could be garbled, use gbk and ignore
        # in linux, no character garbled, use utf-8 is ok
        html = res.read().decode('gbk', 'ignore')
        return html

    def parse_html(self):
        pass
    # save html file

    def save_html(self, filename, html):
        with open(filename, 'w') as f:
            f.write(html)

    # interface function
    def run(self):
        name = input('Name of Tieba: ')
        begin = int(input('Start page: '))
        stop = int(input('stop page: '))
        for page in range(begin, stop+1):
            pn = (page - 1)*50
            params = {'kw': name, 'pn': str(pn)}
    # splice url
            params = parse.urlencode(params)
            url = self.url.format(params)
    # send request
            html = self.get_html(url)
    # define path
            filename ='{}-{}page.html'.format(name, page)
            self.save_html(filename, html)
    # instructions
            print('Page %d has been extracted !'%page)
    # set a time to sleep for 1 - 2 seconds after every page spidering
            time.sleep(random.randint(1, 2))


if __name__=='__main__':
    start = time.time()
    spider = TiebaSpider()
    spider.run()
    end = time.time()
    # check processing time
    print('Processing time: %.2f'%(end-start))







