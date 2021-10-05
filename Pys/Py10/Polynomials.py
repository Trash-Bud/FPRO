# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:59:58 2019

@author: Joana
"""

def evaluate(a, x):
    return sum([ y * x ** a.index(y) for y in a])