# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:47:59 2019

@author: Joana
"""

def lost_element(s1, s2):
    for i in s1:
        if i not in s2:
            return i
    for e in s2:
        if e not in s1:
            return e