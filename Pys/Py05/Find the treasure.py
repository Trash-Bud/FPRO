# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:41:44 2019

@author: Joana
"""

def map(pos, steps):
    pos = list(pos)
    steps = steps.split("-")
    for i in steps:
        if i == "up":
            pos[1] += 1
        elif i == "down":
            pos[1] -= 1
        elif i == "left":
            pos[0] -= 1
        elif i == "right":
            pos[0] += 1
    return tuple(pos)