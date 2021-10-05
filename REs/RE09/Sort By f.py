# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:42:29 2019

@author: Joana
"""

def sort_by_f(alist):
    alist.sort(key = lambda x: (5-x if x>= 5 else x))
    return alist