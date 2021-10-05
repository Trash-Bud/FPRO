# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:38:39 2019

@author: Joana
"""

def rotate_list(l):
    l = l[3:] + l[:3]
    return l