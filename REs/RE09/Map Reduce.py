# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:02:30 2019

@author: Joana
"""
import functools
def map_reduce(n1, n2):
    list1 = [x**2 for x in range(n1,n2) if x % 2 != 0 ]
    return functools.reduce(lambda x, y: x * y if x * y < 50 else x + y, list1)
