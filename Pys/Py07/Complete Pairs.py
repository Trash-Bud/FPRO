# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:34:15 2019

@author: Joana
"""
import string
l = []
def complete_pairs(s1, s2):
    s = string.ascii_lowercase
    for i in s1:
        for f in s2:
            strg = i + f
            for f in s:
                if f not in strg:
                    break
                elif f == "z":
                    l.append(strg)
    for f in s2:
        for t in s:
            if t not in f:
                break
            elif t == "z":
                l.append(f)
    return set(l)
