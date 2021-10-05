# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:05:03 2019

@author: Joana
"""

def bitonic_point(f):
    n = f()
    c = len(n)//2
    i = 2
    ub = len(n)
    lb = 0
    if  n[c-1] < n[c] and n[c] < n[c+1]:
        lb = c
    elif n[c-1] > n[c] and n[c] > n[c+1]:
        ub = c
    else:
        return n[c]
    while i != 0:
        c = lb + (ub- lb)//2
        if n[c-1] < n[c] and n[c] > n[c+1]:
            return n[c]
        elif n[c-1] < n[c] and n[c] < n[c+1]:
            lb = c   
        else:
            ub = c
print(bitonic_point(	lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))