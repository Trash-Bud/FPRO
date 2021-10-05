# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:47:53 2019

@author: Joana
"""

def last_man_standing(alist, step):
    while len(alist) != 1:
        if len(alist) == step:
            bruh = len(alist) - 1
            alist.pop(bruh)
        elif step > len(alist):
            bruh = int(step % len(alist)) -1
            if bruh < 0:
                bruh = len(alist) + bruh
            alist = alist[bruh + 1:] + alist[:bruh]
        else:
            bruh = step -1
            alist = alist[bruh + 1:] + alist[:bruh]
    return alist[0]  