# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:27:24 2019

@author: Joana
"""

def days_until_empty(C, l):
    i = 0
    f = C
    while f > 0:
        i += 1
        f += l
        if f > C:
            f = C
        f -= i
    return i

print(days_until_empty(60,1))
        