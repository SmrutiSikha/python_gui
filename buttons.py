#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:46:03 2019

@author: abhishek
"""
from tkinter import *
but=Tk()
but.title("s")
but.geometry("500x500")
def enter():
    b=a.get()
    l1=Label(text='hi'+' '+b,fg='white',bg='black',font=15).pack()
def delete():
    l2=Label(text='bye',fg='red',bg='pink',font=15).pack()
a=StringVar()
l3=Label(text='surge',fg='red',bg='yellow',font=15).pack()
l4=Label(text='sway',fg='red',bg='yellow',font=15).pack()
b1=Button(text='enter',fg='black',bg='blue',command=enter,font=15).pack()
b2=Button(text='delete',fg='black',bg='green',command=delete,font=15).pack()
text=Entry(textvariable=a,font=10).pack()
but.mainloop()
