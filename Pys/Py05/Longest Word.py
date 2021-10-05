# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:41:22 2019

@author: Joana
"""

def longest(s):
    s = s.split()
    l = [0]
    count = 0
    for i in s:
        count = 0
        for e in i:
            count += 1
        if count > l[0]:
            l[0] = count
    return l[0]
