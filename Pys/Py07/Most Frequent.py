# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:49:43 2019

@author: Joana
"""

def most_frequent(alist):
    dict1 = {}
    l = []
    for i in alist:
        dict1[i] = dict1.get(i, 0) + 1
    for i in dict1:
        l.append([i,dict1[i]])
    l.sort(key = lambda k: (-k[1], -k[0]))
    for i in l:
        res = i[0]
        return res