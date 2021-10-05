# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:34:09 2019

@author: Joana
"""

def treasure(clues):
    f = (0,0)
    for i in range(len(clues)):
        f = clues[f]
        i += i
    return f
        
    