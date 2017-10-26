#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from collections import OrderedDict
import re


def add_key(mydict, a, b, value):
    if a in mydict:
        mydict[a].update({b:value})
    else:
        mydict.update({a:{b:value}})

def get_attrs(attrs, name):
    if len(attrs)!=0:
        for n in attrs:
            if n[0]==name:
                return n[1]

def print_result(myweather, num=2):
    if num>len(myweather):
        num=len(myweather)
    print('----------%s天气----------\n' % city)

    n=0
    for day, data in myweather.items():
        print('%s日, %s' % (day, data['date']))
        if 'high' in data:
            print('%s: %s /%s' % (data['info'], data['high'], data['low']))
        else:
            print('%s: %s' % (data['info'], data['low']))
        print('%s: %s' % (data['wind'], data['level']))
        print()
        n+=1
        if n>num:
            return

def print_comment(myweather):
    n=0
    for day, data in myweather.items():
        if n==0:
            today_high, today_low=int(data['high'][-3:2]), int(data['low'][-3:2])
        if n==1:
            tom_high, tom_low=int(data['high'][-3:2]), int(data['low'][-3:2])
            if tom_high-today_high<-10 or tom_low-today_low<-10:
                print('【明日最高温较今日降低%s°, 最低温降低%s°\n】' % (today_high-tom_high,today_low-tom_low))
            tem_diff=int(data['high'][-3:2])-int(data['low'][-3:2])
            if tem_diff>15:
                print('【明天温差高达%d°，小心感冒】\n' % tem_diff)
            if '雨' in data['info']:
                print('【明天%s，记得带伞】\n' % data['info'])
            return
        n+=1

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.find_info=False
        self.find_high=False
        self.find_low=False
        self.find_wind=False
        self.find_level=False
        self.find_city=False
        self.weather=OrderedDict()
    
    def handle_starttag(self, tag, attrs):
        # 4.风向
        if self.find_wind and self.find_high==False and tag=='span':
            add_key(self.weather, self.day, 'wind', get_attrs(attrs, 'title'))

            self.find_wind=False
            self.find_level=True

    # def handle_startendtag(self, tag, attrs):
    #     pass

    def handle_data(self, data):
        if re.match(r'\d+日（\w{2}）', data):
            self.day=re.match(r'(\d+)日（\w{2}）', data).group(1)
            add_key(self.weather, self.day, 'date', re.match(r'(\d+)日（(\w{2})）', data).group(2))
            self.find_info=True
            self.find_high=True
            self.find_low=True

        if len(data)!=0:
            # 1.天气
            if self.find_info and self.lasttag=='p':
                add_key(self.weather, self.day, 'info', data)
                self.find_info=False
            # 2.高温
            if self.find_high and self.lasttag=='span':
                add_key(self.weather, self.day, 'high', data)
                self.find_high=False
            # 3.低温
            if self.find_low and self.lasttag=='i':
                add_key(self.weather, self.day, 'low', data)
                self.find_low=False
                self.find_high=False

                self.find_wind=True
            # 5.风级
            if self.find_level and self.find_low==False and self.lasttag=='i':
                add_key(self.weather, self.day, 'level', data)
                self.find_level=False

    # def handle_endtag(self, tag):
    #     pass

    # def handle_comment(self, data):
    #     pass

    # def handle_entityref(self, name):
    #     pass

    # def handle_charref(self, name):
    #     pass


parser=MyHTMLParser()
# 这里填写城市编码
city='南京'
city_code='101190101'
with request.urlopen('http://www.weather.com.cn/weather/%s.shtml' % city_code) as f:
    parser.feed(f.read().decode('utf-8'))
    print_comment(parser.weather)
    print_result(parser.weather, 2)
