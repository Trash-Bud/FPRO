# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:59:29 2019

@author: Joana
"""

def sort_by_value(dict):
    l = []
    for i in dict:
        l.append(tuple([i, dict[i]]))
    l.sort(key = lambda k: ( k[1]))
    return l
