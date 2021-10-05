# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:37:08 2019

@author: Joana
"""

def find_me(f, limits):
    i = 0
    midf = limits[1]
    midi = limits[0]
    mid = (midf - midi)/2 + midi  
    c = f(mid)
    while c != 0:
        if c < 1:
            i += 1
            midf = mid
            mid = int((midf - midi)/2 + midi)  
        else:
            i += 1
            midi = mid
            mid = int((midf - midi)/2 + midi )        
        c = f(mid)
    return i
    