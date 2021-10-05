# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:12:25 2019

@author: Joana
"""

def sum_digits_rec(n):
    if type(n) == int:
        n = [int(x) for x in str(n)]
    else:
        pass
    if len(n) == 1:
        return int(n[0])
    else:
        return int(n[0]) + sum_digits_rec(n[1::])

        