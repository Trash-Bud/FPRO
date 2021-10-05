# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:00:23 2019

@author: Joana
"""
import math
def juggler(n, p):   
    if p == 0:
        return n
    elif juggler(n, p-1) % 2 == 0:
        return math.floor((juggler(n,p-1))**(1/2))

    else:
        return math.floor((juggler(n,p-1))**(3/2))