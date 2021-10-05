# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:33:50 2019

@author: Joana
"""

def C(n, r):
    R = 1
    Df = 1
    for i in range(0, r):
        D1 = (n - i)
        Df = Df * D1 
    for e in range(1, r + 1):
        R = R * e
    C = Df/R  
    return (C)