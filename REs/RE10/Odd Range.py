# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:43:37 2019

@author: Joana
"""

def odd_range(start, stop, step):
    l = [ x for x in range(start, stop) if x % 2 != 0]
    for x in l:
        if l.index(x) % step == 0:
            yield x


print(list(odd_range(0, 20, 2)))
    
