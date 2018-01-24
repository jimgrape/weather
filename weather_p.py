#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 日期、相对天数、天气情况、高温、低温、风向、风级
from weather import myweather
import sys

def print_result(myweather, num=2):
    if num == 0:
        print('%s: %s°/%s°, %s: %s' % (myweather[0]['info'], myweather[0]['high'], myweather[0]['low'], myweather[0]['wind'],myweather[0]['level']))
        return
    if num>len(myweather):
        num=len(myweather)
    print('----------%s天气----------\n' % city)
    n=0
    for item in myweather:
        print('%s, %s' % (item['date'], item['rela']))
        print('%s: %s°/%s°' % (item['info'], item['high'], item['low']))
        print('%s: %s' % (item['wind'], item['level']))
        print()
        n+=1
        if n>num:
            return

city='南京'

if __name__=='__main__':
    if len(sys.argv)>=2:
        num=int(sys.argv[1])
        print_result(myweather, num)
    else:
        print_result(myweather)

