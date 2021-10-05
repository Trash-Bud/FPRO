# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:04:12 2019

@author: Joana
"""

def pattern_hunting(l1, l2, p):
    l = []
    for e in range(len(l2)):
        if p in l2[e]:
            l.append(l1[e]) 
    for e in range(len(l1)):
        if p in l1[e]:
            l.append(l2[e]) 
    l.sort(reverse = True)
    return l