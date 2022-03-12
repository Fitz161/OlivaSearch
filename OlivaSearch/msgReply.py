# -*- encoding=utf8 -*-

import urllib

import requests
from lxml import etree

from OlivaSearch.config import *

command_dict = {}


def add_command(command):
    """ 命令的装饰器 """
    def add_func(func):
        command_dict[command] = func
    return add_func


@add_command('帮助')
def help_doc(plugin_event, _):
    return HELP_DOC


@add_command('help')
def help_doc(plugin_event, _):
    return HELP_DOC


def get_one_page(url, type='text'):
    """ 使用get请求访问指定url，并根据type以指定形式返回网页内容 """
    headers = {
        "User-Agent": USER_AGENT}
    try:
        response = requests.get(url, headers=headers, timeout=8)
        if response.status_code == 200 or response.status_code == 304:
            if type == 'text':
                return response.text
            elif type == 'json':
                return response.json()
            elif type == 'content':
                return response.content
        else:
            return "failed"
    except requests.RequestException as e:
        return "time_out"


def parse_one_page(text, option):
    """ 对网页进行解析 """
    html = etree.HTML(text, etree.HTMLParser())
    content = html.xpath(XPATH_DICT[option])
    string = ''
    for item in content:
        string += item.xpath('string(.)').replace('\n', '')
    return string


def search(url, type, item):
    html = get_one_page(url)
    if html == 'failed':
        return "搜索 %s 失败\n该条目不存在" % item
    elif html == 'time_out':
        return "搜索 %s 超时，请重试" % item
    else:
        result = parse_one_page(html, type)
        if result is None:
            return "搜索 %s 失败\n没有该条目" % item
        else:
            return "搜索 %s :\n%s" % (item, result)


@add_command('百度')
def baidu(plugin_event, _):
    message = plugin_event.data.message
    if message[2] != ' ': return #第三个字符必须是空格
    item = message[2:].strip()
    url = SERACH_BASE_URL['baidu'] + urllib.parse.quote(item)
    return search(url, 'baidu', item)


@add_command('搜索')
def search_item(plugin_event, _):
    message = plugin_event.data.message
    if len(message) >= 3 and message[2].isdigit():
        search_type = TYPE_TRANS.get(int(message[2]))
    else:
        if message[2:].strip() in command_dict.keys() and \
                message[2:].strip() not in ['搜索', '百度']:
            return command_dict.get(message[2:].strip())(plugin_event, _)
        return
    keyword = message[3:].strip()
    if search_type:
        url = SERACH_BASE_URL[search_type] + urllib.parse.quote(keyword)
        return search(url, search_type, keyword)


def unity_init(_, Proc):
    Proc.log(
        log_level=2,
        log_message='OlivaSearch已成功加载',
        log_segment=[
            ('OlivaSearch', 'default'),
            ('Init', 'default')
        ]
    )


def unity_reply(plugin_event, Proc):
    message = plugin_event.data.message
    if message[:2] not in ['搜索', '百度'] or len(message) < 3: return
    reply_msg = command_dict.get(message[:2])(plugin_event, Proc)
    if not reply_msg: return
    plugin_event.reply(reply_msg[:MAX_SEND_LENGTH])
