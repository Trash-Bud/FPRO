# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:40:59 2019

@author: Joana
"""

def count_until(tup):
    count = 0
    for i in tup:
        if type(i) is tuple: 
            return count
        count += 1
    if count == len(tup):
        return -1