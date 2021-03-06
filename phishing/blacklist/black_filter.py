#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re


def get_rank(search_url):
    url = 'http://data.alexa.com/data?cli=10&url=%s' % search_url
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                             '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Upgrade-Insecure-Requests': '1'
               }
    try:
        xml = requests.get(url, headers=headers).text
        return re.compile(r'<REACH RANK="\d+"/>').search(xml).group()
    except Exception, e:
        print 'There are not Rank.'
        return

print get_rank('www.baidu.com')