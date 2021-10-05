# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:40:32 2019

@author: Joana
"""

def bagdiff(xs,ys):
    for i in xs:
        for e in ys:
            if i == e:
                xs.remove(i)
                ys.remove(i)
    return xs

