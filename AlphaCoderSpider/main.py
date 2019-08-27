from AlphaCoderSpider.spider import search
from AlphaCoderSpider.web import web_start

if __name__ == '__main__':
    search('Darling In The Franxx')
    print('Ok..')
    web_start('127.0.0.1', 23333)

