# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:03:50 2020

@author: Joana
"""

def find_dtype(atuple, data_type):
    l = []
    for i in atuple:
        t_str = str(type(i))
        print(t_str)
        if data_type not in t_str:
            pass
        else:
            l.append(i)
    return tuple(l)