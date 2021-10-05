# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:19:52 2019

@author: Joana
"""
import functools
def evaluate(a, x):
    f = list(map(lambda y: y *(x ** a.index(y)),a))
    return int(functools.reduce(lambda a,b: a+b,f))