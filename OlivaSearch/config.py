# -*- encoding=utf8 -*-

MAX_SEND_LENGTH = 200

HELP_DOC = '''
搜索[格式] [待搜索关键词]
可用搜索格式:
百度/搜索1：百度百科
搜索2：萌娘百科
搜索3：touhouwiki
搜索4：wikipedia
'''

XPATH_DICT = {
    'baidu': '/html/body/div[3]/div[2]/div/div[1]/div[4]/div',
    'moe': '//*[@id="mw-content-text"]/div/p',
    'touhou': '//*[@id="mw-content-text"]/div/div[1]/p[position()<3]',
    'wiki': '//*[@id="mw-content-text"]/div/p'
}

SERACH_BASE_URL = {
    'baidu': 'https://baike.baidu.com/item/',
    'moe': 'https://zh.moegirl.org/',
    'touhou': 'https://thwiki.cc/',
    'wiki': 'https://zh.wikipedia.org/wiki/'}

TYPE_TRANS = {
    1: 'baidu',
    2: 'moe',
    3: 'touhou',
    4: 'wiki'}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'