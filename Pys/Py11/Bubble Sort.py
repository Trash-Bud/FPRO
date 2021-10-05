# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:43:24 2019

@author: Joana
"""

def bubble_sort(alist):
    for i in range(len(alist)):
        for e in range(i + 1):
            if alist[i] < alist[e]:
                a = alist[e]
                alist[e] = alist[i]
                alist[i] = a
    return alist