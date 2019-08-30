import requests
import re
import json
import multiprocessing
from AlphaCoderSpider.config import store

links = {}


def search(keyword):
    global links
    s = requests.session()
    url = 'https://wall.alphacoders.com/search.php?search={}'.format(keyword)
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36',
    }
    res = s.get(url, headers=headers)
    content = res.text
    max_page = get_max_page(content)
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    for page in range(1, int(max_page) + 1):
        result = pool.apply_async(get_download_links, args=(page, keyword))
        # print(result.get())
    pool.close()
    pool.join()


def get_download_links(page, keyword):
    results = dict()
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36',
    }
    s = requests.session()
    url = 'https://wall.alphacoders.com/search.php'
    payload = {'search': keyword, 'page': page}
    res = s.get(url, params=payload, headers=headers)
    content = res.text
    ids = get_ids(content)
    for image_id in ids:
        url = 'https://wall.alphacoders.com/big.php?i={}'.format(image_id)
        res = s.get(url, headers=headers)
        content = res.text
        result = get_data(content)
        image_type = result[0]
        server = result[1]
        user_id = result[2]
        url = 'https://wall.alphacoders.com/get_download_link.php'
        data = {
            'wallpaper_id': image_id,
            'type': image_type,
            'server': server,
            'user_id': user_id
        }
        res = s.post(url, headers=headers, data=data)
        link = res.text
        results[image_id] = link
    store(json.dumps(results))

def get_max_page(content):
    regex = r"<input type=\"text\" class=\"form-control\" placeholder=\"Page # / \d+\">"
    matches = re.findall(regex, content)
    if matches:
        text = matches[0]
        regex = r"\d+"
        match = re.findall(regex, text)
        return match[0]
    else:
        return 1


def get_ids(content):
    result = []
    regex = r"<div class=\"thumb-container-big \" id=\"thumb_\d+\">"
    matches = re.findall(regex, content)
    if matches:
        for match in matches:
            regex = r"\d+"
            image_id = re.findall(regex, match)[0]
            result.append(image_id)
        return result
    else:
        print('ERROR TO MATCH IMAGE ID Or No ID')


def get_data(content):
    result = []
    regex = r"data-type=\"\S+\""
    image_type = re.findall(regex, content)[0].replace('\"', '')[10:]
    regex = r"data-server=\"\S+\""
    server = re.findall(regex, content)[0].replace('\"', '')[12:]
    regex = r'data-user-id=\"\d+\"'
    user_id = re.findall(regex, content)[0].replace('\"', '')[13:]
    result.append(image_type)
    result.append(server)
    result.append(user_id)
    return result




