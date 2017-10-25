#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
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

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.find_info=False
        self.find_high=False
        self.find_low=False
        self.find_wind=False
        self.find_level=False
        self.weather={}
    
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
print('[南京天气]\n')
with request.urlopen('http://www.weather.com.cn/weather/101190101.shtml') as f:
    parser.feed(f.read().decode('utf-8'))
    print(parser.weather)
