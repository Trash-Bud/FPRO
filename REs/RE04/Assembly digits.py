# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:51:26 2020

@author: Joana
"""

def adigits(n1, n2, n3):
    n1i = int(n1)
    n2i = int(n2)
    n3i = int(n3)
    l1 =[]
    for i in range(0, n1i):
        if i == n2i:
           l1.append("2 smaller")
        if i == n3i:
           l1.append("3 smaller")
        else:
            pass  
    if len(l1) == 2:
        if n2i > n3i:
            n = int(n1 + n2 + n3)
        else:
            n = int(n1 + n3 + n2)
    elif len(l1) == 1:
        if l1[0] == "2 smaller":
            n = int(n3 + n1 + n2)
        else:
            n = int(n2 + n1 + n3)     
    else:
        if n2i > n3i:
            n = int(n2 + n3 + n1)
        else:
            n = int(n3 + n2 + n1)
    return n