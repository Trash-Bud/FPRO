# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:37:45 2019

@author: Joana
"""

import math
def pascal(n):
    w= ""
    for i in range(n):
        l = []
        for j in range(i+1):
            c = math.factorial(i)/(math.factorial(j)*math.factorial(i-j))
            l.append(c)
        for e in range(len(l)):
            if e == len(l)-1:
                w += str(int(l[e])) + "\n"
            else:
                w += str(int(l[e])) + " "
    return w