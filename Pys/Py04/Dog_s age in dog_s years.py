# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:35:53 2019

@author: Joana
"""

def dogs(h_age):
    if h_age <= 2:
        agef = h_age * 10.5
    else: 
        rest = h_age - 2
        age1st = 2 * 10.5
        agerest = rest * 4
        agef = agerest + age1st
    return agef