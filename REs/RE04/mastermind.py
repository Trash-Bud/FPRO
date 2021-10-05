# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:55:46 2020

@author: Joana
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    l1 = [g1, g2, g3]
    l2 = [c1, c2, c3]
    points = 0
    for i in range(0, 3):
        if l1[i] == l2[i]:
            points += 3
            l1[i] = i + 3
            l2[i] = i - 3
        else:
            pass
    for i in range(0, 3):
         if l1[i] in l2:
            points += 1 
            e = l2.index(l1[i])
            l1[i] = i + 3
            l2[e] = i - 3 
         else:
            pass
                  
    return points