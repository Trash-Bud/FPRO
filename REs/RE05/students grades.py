# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:05:22 2020

@author: Joana
"""

def sort_grades(records):
    
    return tuple(sorted(records, key = lambda k: (100 - (sum(list(k[2]))/len(list(k[2]))), k[0], k[1])))