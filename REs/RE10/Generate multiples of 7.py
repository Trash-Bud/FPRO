# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:43:39 2019

@author: Joana
"""

def multiples_of7(n):
    t = 0
    while t < n:
        if t % 7 == 0:
            yield t
        t += 1
            
print(list(multiples_of7(21)))
            