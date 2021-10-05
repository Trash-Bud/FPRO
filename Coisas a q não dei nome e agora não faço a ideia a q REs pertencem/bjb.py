# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:33:43 2019

@author: Joana
"""

def greaters(num):
    l = []
    w = ""
    for i in str(num):
        l.append(i)
    l.sort(reverse = True)
    for i in l:
        w += str(i)
    return int(w)

print(greaters(310909))