# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:48:46 2019

@author: Joana
"""

def fetch_middle(llists):
    fl=[]
    for i in llists:
        if len(i) % 2 == 0:
            fl.append((i[int(len(i)/2 - 1)] + i[int(len(i)/ 2)])/2)
        else:
            fl.append(i[int(len(i)/2)])
    return fl