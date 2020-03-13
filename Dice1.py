# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:44:11 2020
@author: admin
"""
import os
os.chdir('E:/business1')
from tkinter import *
import random
def dice():
    d=random.randrange(1,7)
    print("Dice: "+str(d))
    return d
    a=0
    b=0
    while a+b!=d:        
        a=random.randrange(1,7)
        b=random.randrange(1,7)
    return d,a,b