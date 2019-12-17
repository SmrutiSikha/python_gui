#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 10:03:06 2019

@author: abhishek
"""

from tkinter import *
myGui=Tk()
myGui.title("chutiya")
myGui.geometry("300x300")
mymenu=Menu()
list1=Menu()
list2=Menu()
list1.add_command(label="new file")
list1.add_command(label="open")
list1.add_command(label="save")
list2.add_command(label="undo")
list2.add_command(label="copy")
list2.add_command(label="cut")
mymenu.add_cascade(label="File",menu=list1)
mymenu.add_cascade(label="Edit",menu=list2)
mymenu.add_cascade(label="Run")
myGui.config(menu=mymenu)
myGui.mainloop()