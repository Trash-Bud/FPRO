# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:06:05 2019

@author: Joana
"""

def to_celsius(t):
    return list(map(lambda x: round((x-32)*5/9,1),t))

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]	))