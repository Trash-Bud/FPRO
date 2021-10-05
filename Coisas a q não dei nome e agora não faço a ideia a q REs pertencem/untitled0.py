# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:59:24 2019

@author: Joana
"""

import math
def local_minima(alist, n):
    l1 = []
    l2 = []
    i = 0
    f = []
    t = math.ceil(len(alist) / n)
    for e in range(len(alist)):
        l1.append(alist[e])
        i += 1
        if len(l1) == 3:
            l1.sort()
            l2 = alist[(e-2):e+1]
            l3 = [l1[0],e - l2.index(l1[0])]
            f.append(tuple(l3))
            i = 0
            l1 = []
        elif e == len(alist) - 1 :
            l1.sort()
            l2 = alist[e-i+1:e+1]
            l3 = [l1[0],e - l2.index(l1[0])]
            f.append(tuple(l3))   
    return f
print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))