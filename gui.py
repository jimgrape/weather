#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from weather import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel=Label(self, text='南京天气')
        self.helloLabel.pack()

        self.alertButton=Button(self, text='显示', command=self.show_result(parser.weather)
        self.alertButton.pack()

        self.quitButton=Button(self, text='退出', command=self.quit)
        self.quitButton.pack()

    def show_result(myweather, num=2):
        if num>len(myweather):
            num=len(myweather)
        w_result+='----------%s天气----------\n' % city

        n=0
        for day, data in myweather.items():
            w_result+='%s日, %s' % (day, data['date'])
            if 'high' in data:
                w_result+='%s: %s /%s' % (data['info'], data['high'], data['low'])
            else:
                w_result+='%s: %s' % (data['info'], data['low'])
            w_result+='%s: %s' % (data['wind'], data['level'])
            n+=1
            if n>num:
                return
        self.resultLabel=Label(self, text=w_result)
        self.resultLabel.pack()


app=Application()
app.master.title('天气')
app.mainloop()
