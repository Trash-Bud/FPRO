# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:37:14 2019

@author: Joana
"""

def no_consecutives1(k):
    if k == 0:
        return 0
    elif k == 1:
        return 2
    elif k == 2:
        return 3
    else:
        return no_consecutives1(k - 1 ) + no_consecutives1(k - 2)