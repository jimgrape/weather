#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request 
import re

def add_key(mydict, a, b, value):
    if a in mydict:
        mydict[a].update({b:value})
    else:
        mydict.update({a:{b:value}})

def get_content(city_code):
    with urllib.request.urlopen('http://www.weather.com.cn/weather/%s.shtml' % city_code) as f:
        html = f.read().decode('utf-8')
        return html

# 获取关键数据
def get(html):
    # 日期、相对天数、天气情况、高温、低温、风向、风级
    reg = re.compile(r'li class="sky skyid.*?<h1>(.*?)（(.*?)）</h1>.*?<p title="(.*?)".*?<span>(.*?)℃</span>.*?<i>(.*?)℃</i>.*?<span title="(.*?)".*?</em>\n<i>(.*?)</i>', re.S)
    items = re.findall(reg, html)
    return items

# 数据处理
def write_result(items):
    myweather = []
    key = ['rela', 'info', 'high', 'low', 'wind', 'level']
    for item in items:
        myweather.append({item[0]:dict(zip(key, item[1:]))})
    return myweather

# 这里填写城市编码
city_code='101190101'
myweather=write_result(get(get_content(city_code)))
if __name__ == '__main__':
    print(myweather) 
