# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:39:14 2019

@author: Joana
"""

def greatest(num):
    num = str(num)
    l = []
    w = ""
    for i in num:
        l.append(i)
    l.sort(reverse = True)
    for i in l:
        w = w + i
    return int(w)