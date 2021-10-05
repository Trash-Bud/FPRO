# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:33:41 2019

@author: Joana
"""

def rearrange(l):
    return [x for x in l if x <= 0] + [x for x in l if x>0]