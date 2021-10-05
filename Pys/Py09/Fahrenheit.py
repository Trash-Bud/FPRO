# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:10:40 2019

@author: Joana
"""

def to_fahrenheit(t):
    return list(map(lambda x: round((x*9/5) +32,2),t))

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]	))