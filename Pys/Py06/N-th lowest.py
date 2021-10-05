# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:36:46 2019

@author: Joana
"""

def nth_lowest(lnum, n):
    lnum.sort()
    return lnum[n-1]