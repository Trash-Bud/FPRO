# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:19:05 2019

@author: Joana
"""

def is_orthogonal(mx):
    i = 0
    for f in mx:
        if abs(f[i]) != 1:
            return False
        for s in f[i+1:]:
            if s != 0:
                return False
        for t in f[:i]:
            if t != 0:
                return False
        i += 1
    return True
        
    