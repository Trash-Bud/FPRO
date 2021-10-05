# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:03:25 2019

@author: Joana
"""

def get_composites(n):
    for x in range(4,n+1):
        y = 2
        while y < n+1:
            if  x % y == 0 and y!= x:
                yield x
                break
            y += 1

print(list(get_composites(6)))