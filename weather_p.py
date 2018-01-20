#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from weather2 import myweather
import sys

def print_result(myweather, num=2):
    if num == 0:
        print('%s, %s:%s/%s' % (
    if num>len(myweather):
        num=len(myweather)
    print('----------%s天气----------\n' % city)

    n=0
    for day, data in myweather:
        print('%s日, %s' % (day, data['date']))
        if 'high' in data:
            print('%s: %s°/%s°' % (data['info'], data['high'], data['low']))
        else:
            print('%s: %s°' % (data['info'], data['low']))
        print('%s: %s' % (data['wind'], data['level']))
        print()
        n+=1
        if n>num:
            return

def print_comment(myweather):
    n=0
    for day, data in myweather.items():
        if n==1:
            tom_high, tom_low=int(data['high']), int(data['low'])
            tem_diff=int(data['high'])-int(data['low'])
            if tem_diff>15:
                print('【明天温差高达%d°，小心感冒】\n' % tem_diff)
            if '雨' in data['info']:
                print('【明天%s，记得带伞】\n' % data['info'])
            return
        n+=1

city='南京'

if __name__=='__main__':
    if len(sys.argv)>=2:
        num=int(sys.argv[1])
        print_result(myweather, num)
    else:
        print_result(myweather)

