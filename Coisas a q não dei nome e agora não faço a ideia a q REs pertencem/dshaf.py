# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:13:49 2019

@author: Joana
"""
import string
def split(word): 
    return [char for char in word] 

def anagrams(alist):
    lf = []
    la = []
    for i in alist:
        la.append(i)
        l1 = split(i)
        for e in alist[alist.index(i) + 1::]:
            l2 = split(e)
            for f in l2:
                l1 = split(i)
                if f in l1 and len(l1) == len(e):
                    l1[l1.index(f)] = "00"
                elif f not in l1 or len(l1) != len(e):
                    pass
                else:
                    la.append(e)
        lf.append(la)
        la = []
    return lf

print(anagrams(	['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']))

string.Formatter()