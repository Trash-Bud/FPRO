# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:12:17 2019

@author: Joana
"""

def bisect(f, n):
    i = 0
    lb = 0 
    ub = 1
    while i != n:
        mid = (ub + lb) /2
        if (f(lb) < 0 and f(mid) < 0) or (f(lb) > 0 and f(mid) > 0):
            lb = mid
        else:
            ub = mid
        i += 1
    return round(mid,5)

print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))
            
        