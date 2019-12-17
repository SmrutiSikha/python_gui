#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:15:14 2019

@author: abhishek
"""
from tkinter import *
a=Tk()
a.title("s")
a.geometry("500x500")
l1=Label(text='surge',fg='red',bg='yellow').pack()
l2=Label(text='sway',fg='red',bg='yellow').pack()
a.mainloop()
########################
grid=Tk()
grid.title="smruti"
grid.geometry("500x500+100+100")
label1=Label(text='apple',font=10).place(x=50,y=50)
label2=Label(text='banana',font=50).grid(row=0,column=0)
label3=Label(text='orange',font=50).grid(row=1,column=0)
grid.mainloop()
#########################
but=Tk()
but.title("s")
but.geometry("500x500")
l3=Label(text='surge',fg='red',bg='yellow',font=15).pack()
l4=Label(text='sway',fg='red',bg='yellow',font=15).pack()
b1=Button(text='enter',fg='black',bg='blue').pack()
b2=Button(text='delete',fg='black',bg='green').pack()
but.mainloop()
