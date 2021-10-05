# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:32:23 2019

@author: Joana
"""

def map(pos,steps):
    if steps == []:
        return pos
    if steps[0] == "right":
        pos = tuple( [pos[0] + 1, pos[1]])
        return map(pos, steps[1::])
    elif steps[0] == "left":
        pos = tuple([pos[0]-1, pos[1]])
        return map(pos, steps[1::])        
    elif steps[0] == "up": 
        pos = tuple( [pos[0], pos[1] + 1])
        return map(pos, steps[1::])
    elif steps[0] == "down": 
        pos = tuple( [pos[0], pos[1]-1])
        return map(pos, steps[1::])