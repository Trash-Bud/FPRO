# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:51:21 2019

@author: Joana
"""

def override(l1, l2):
    l3 = [x[0] for x in l2]
    result = l2 + [k for k in l1 if k[0] not in l3]
    return sorted(result, key = lambda k: k[0])