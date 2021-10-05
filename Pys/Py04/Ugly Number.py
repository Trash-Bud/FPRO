# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:39:53 2019

@author: Joana
"""

def ugly(n):
    l = []
    for i in range(2, n):
        n1 = n%i
        if n1 == 0:
            l.append(i)
    if n == 1:
        return True
    elif (2 in l or 3 in l or 5 in l) and len(l) == 1:
        return True
    elif ((2 in l and 3 in l) or (2 in l and 5 in l) or (5 in l and 3 in l)) and len(l) == 2:
        return True
    elif 2 in l and 3 in l and 5 in l and len(l) == 3:
        return True
    else:
        return False