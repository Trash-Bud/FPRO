# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:01:12 2019

@author: Joana
"""

def to_celsius(t):
    return[round((x-32)*5/9,1) for x in t]