# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:15:04 2019

@author: Joana
"""
import functools
def map_filter_reduce(lst, f1, f2, f3):
    lst = filter(f1,lst)
    lst = map(f2,lst)
    return functools.reduce(f3,lst)