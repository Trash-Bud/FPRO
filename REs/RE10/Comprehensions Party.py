# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 11:56:03 2019

@author: Joana
"""
import math
def comprehensions(i, j):
    n = ["3", "8"]
    l1 = [str(x) for x in range(i,j+1)]
    l = tuple([[int(x) for x in l1 if x[len(x)-1] in n] ,tuple([round(math.sqrt(x),2) for x in range(i,j+1)]),{x:chr(x) for x in range(i,j+1)}])
    return l