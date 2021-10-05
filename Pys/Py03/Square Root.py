# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:32:55 2019

@author: Joana
"""

n = int(input())
a = 0
b = n
mid_p = (a + b)/2
if n == mid_p * mid_p:
    print(mid_p)
else:
    while n != mid_p * mid_p and abs(a-b) > 1e-5:
        if mid_p * mid_p > n:
            b = mid_p
        else:
            a = mid_p
        mid_p = (a + b)/2
    print(round(mid_p, 5))
     