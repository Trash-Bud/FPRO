# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:14:54 2019

@author: Joana
"""

def brute_force(f, l):
    q =[i + j + k for i in l  
                  for j in l 
                  for k in l]
    l1 = filter(f, q)
    return list(l1)