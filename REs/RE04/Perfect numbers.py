# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:51:02 2020

@author: Joana
"""

def is_perfect(n):
    l =[]
    for i in range(1, n):
        resto = n % i
        if resto == 0:
            l.append(i)
        else:
            pass
    sum = 0
    for i in range(0, len(l)):
        sum += l[i]
    if sum == n:
        result = True
    else:
        result = False
    return result

        