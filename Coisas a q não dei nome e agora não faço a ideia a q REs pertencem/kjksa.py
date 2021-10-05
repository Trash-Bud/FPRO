# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:44:42 2019

@author: Joana
"""
l = input()
def genealogy(l):
    return list(sorted(l, key = lambda k: (k[1], k[0])))


print(genealogy(l))