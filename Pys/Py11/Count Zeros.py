# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:35:26 2019

@author: Joana
"""

def count_zeros(f):
    f = f()
    i = 2
    lb = 0
    ub = len(f)
    n = lb + (ub - lb)//2
    if f[n] == 1:
        lb = n
    else:
        ub = n
    while i != 0:
        n = lb + (ub - lb)//2
        if (f[n] == 0 and f[n - 1] == 1):
            return len(f) - n
        elif (f[n] == 1 and f[n + 1] == 0):
            return len(f) - (n + 1)
        elif f[n] == 1:
            lb = n      
        else:
            ub = n
            
print(count_zeros(lambda: [1]*80000000 + [0]*70000000))