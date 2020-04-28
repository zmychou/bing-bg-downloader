from urllib.request import Request, urlopen
import base64
import os
import re
import time

from github_operations import *

BASE_URL = 'https://cn.bing.com'#'https://www.bing.com/?mkt=zh-CN'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
              'KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
IMAGE_BASE64_REG = r'(?<=url\(data:image/png;base64,)[0-9a-zA-Z/=+]{0,65535}(?=\))'
IMAGE_HREF_REG = r'(?<=href=\")[0-9a-zA-Z/\?\-=._]{10,100}jpg'
TITLE_REG = r'(?<=title=\")[\u4e00-\u9fa5\x00-\xff，。？：；、]{1,100}\(©[0-9a-zA-Z\/\+\ ]{2,100}\)'
RELATIVE_SEARCH_REG = r'(?<=href=\")/search\?q[%0-9a-zA-F&;=-]{0,100}'

def get_page_source(url, to_string=True):
    req = construct_request(url)
    resp = urlopen(req)
    page_raw = resp.read()
    if to_string:
        return bytes.fromhex(page_raw.hex()).decode('utf-8')
    else:
        return page_raw
    
    
def construct_request(url, header=None, method='GET'):
    if not header:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'\
            'Chrome/81.0.4044.113 Safari/537.36'
            
        }
    req = Request(url=url, headers=header, method=method)

    return req

def get_image_base64(text):
    reg = re.compile(IMAGE_BASE64_REG)
    matchs = reg.findall(text)
    return matchs

def get_content_by_reg(text, reg):
    reg = re.compile(reg)
    matchs = reg.findall(text)
    return matchs
    
def save(base64s):
    time_str = time.strftime('%Y%m%d')
    for i, b in enumerate(base64s):
        file_name = '{}_{}.png'.format(time_str, i)
        
        img = base64.b64decode(b)
        with open(file_name, 'wb') as f:
            f.write(img)
            
def complete_image_url(relative):
    return '{}{}&rf=LaDigue_1920x1080.jpg&pid=hp'.format(BASE_URL, relative)


def download_image(urls, title):
    month = time.strftime('%Y%m')
    dirs = os.path.join('images', month)
    os.makedirs(dirs, exist_ok=True)
    time_str = time.strftime('%Y%m%d')
    for i, u in enumerate(urls):
        file_name = '{}_{}_{}.jpg'.format(title[0], time_str, i)
        file_name = file_name.replace('/', '_')
        file_name = file_name.replace(' ', '_')
        file_name = os.path.join(dirs, file_name)
        url = complete_image_url(u)
        raw = get_page_source(url, False)
        with open(file_name, 'wb') as f:
            f.write(raw)
        log('Downloaded ' + file_name)
            

def log(msg):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    m = '[{}] {}\n'.format(time_str, msg)
    print(m)
    os.makedirs('log', exist_ok=True)
    with open('log/log.txt', 'a') as f:
        f.write(m)
    
def on_error(text, error_msg):
    
    time_str = time.strftime('%Y-%m-%d-%H-%M-%S')
    file_name = time_str + '-error.txt'
    with open(file_name, 'w') as f:
        f.write(text)
    log(error_msg + 'see ' + file_name)
        
    
if __name__ == '__main__':
    page_raw = get_page_source(BASE_URL)
    image_title = get_content_by_reg(page_raw, TITLE_REG)
    img_links = get_content_by_reg(page_raw, IMAGE_HREF_REG)
    print(image_title)
    try:
        download_image(img_links, image_title)
    except IndexError:
        on_error(page_raw, 'Error occur! ')

    git_add('.')
    git_commit(image_title)
    git_push('origin', 'master')
