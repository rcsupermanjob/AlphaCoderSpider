import httpx
import re
import json
from loguru import logger
from parse import *

logger.add("log-{time}", format="{time} {level} {message}", level="INFO", backtrace=True,
           diagnose=True, enqueue=True, rotation='500MB', encoding='utf8')


class Spider:
    def __init__(self, keyword):
        self.keyword = keyword
        self.client = httpx.Client(trust_env=False)

    def search(self):
        url = 'https://wall.alphacoders.com/search.php?search={}'.format(self.keyword)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/76.0.3809.100 Safari/537.36',
        }
        response = self.client.get(url, headers=headers).text
        match = search('" placeholder="Page # / {:d}"', response)
        max_page = match[0] if match else 0
        for page in range(1, max_page + 1):
            self.get_download_links(page, self.keyword)

    def get_download_links(self, page, keyword):
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/76.0.3809.100 Safari/537.36',
        }
        url = 'https://wall.alphacoders.com/search.php'
        params = {'search': keyword, 'page': page}
        response = self.client.get(url, params=params, headers=headers).text
        ids = findall('<div class="thumb-container-big " id="thumb_{:d}">', response)
        for image_id in ids:
            url = 'https://wall.alphacoders.com/big.php?i={}'.format(image_id[0])
            response = self.client.get(url, headers=headers).text
            image_type = search('data-type="{}"', response)[0]
            server = search('data-server="{}"', response)[0]
            url = 'https://api.alphacoders.com/content/get-download-link'
            data = {
                'content_id': image_id[0],
                'file_type': image_type,
                'image_server': server,
                'content_type': 'wallpaper'
            }
            link = self.client.post(url, headers=headers, data=data).json()['link']
            logger.info(link)
