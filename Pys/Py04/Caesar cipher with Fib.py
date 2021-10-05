# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:38:33 2019

@author: Joana
"""

import math
def caesar(message):
    l1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    l2 = []
    w = ""
    for n in range(len(message)):
        if message[n] == " " or message[n]=="!" or message[n]=="?" or message[n]==".":
            l2.append(message[n])
        else:
            position = ((1 + math.sqrt(5))**n - (1-math.sqrt(5))**n)/(2**n * math.sqrt(5))
            ind = l1.index(message[n])
            idx = ind - position
            idx_mod = math.ceil(idx) % 26
            cyph = l1[abs(math.ceil(idx_mod))]
            l2.append(cyph)
    for e in l2:
        w = w + e
    return w