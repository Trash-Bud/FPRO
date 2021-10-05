# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:36:28 2019

@author: Joana
"""

import math
def solver(a, b, c):
    l=[]
    if (b**2 - 4*a*c) < 0:
        return l
    else:
        pass
    s1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    s2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    
    if s1 == s2:
        l.append(s1)
        return l
    else:
        l.append(s1)
        l.append(s2)
    return sorted(l)