# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:59:59 2019

@author: Joana
"""

def gcd_rec(n2, n1):
    s = n1 - n2 * (n1//n2)
    if s == 0:
        return n2
    else:
        return gcd_rec(s, n2)