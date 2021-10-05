# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:59:29 2019

@author: Joana
"""

def min_path(path):
    init = [0,0]
    i = [0,0]
    l = []
    for e in path:
        if e == "UP":
            i[1] += 1
        elif e == "DOWN":
            i[1] -= 1
        elif e == "LEFT":
            i[0] -= 1
        elif e == "RIGHT":
            i[0] += 1
    if i[1]> 0:
       while i[1] != 0:
           l.append("UP")
           i[1] -= 1
    else:
       while i[1] != 0:
           l.append("DOWN")
           i[1] += 1
    if i[0]> 0:
       while i[0] != 0:
           l.append("RIGHT")
           i[0] -= 1
    else:
       while i[0] != 0:
           l.append("LEFT")
           i[0] += 1
    if l == []:
        return path
    else:
        l.sort(key = lambda k: (path.index(k)))
        return l