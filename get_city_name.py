#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过百度搜索，获得相关城市在中国天气网的编号

from urllib import request

#city=input('Please enter the city: ')

req=request.Request('https://www.baidu.com/s?wd=南京天气')
req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')  

with request.URLopener(req) as bd_weather:
    print(bd_weather.read().decode('utf-8'))
#    with open('1.html', 'w') as f:
#        f.write(bd_weather.read())
