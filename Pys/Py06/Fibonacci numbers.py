# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:31:10 2019

@author: Joana
"""

def fib(n):
    l = [0, 1]
    if n == 1:
        l = [0]
        return l
    else:
        for i in range(1, n -1):
           l.append(l[i-1] + l[i])
        return l 
print(fib(5))