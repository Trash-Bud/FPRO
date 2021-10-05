# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:38:08 2019

@author: Joana
"""

def collatz(n):
    l = [n]
    w = ""
    while n != 1:
        if n%2 == 0:
            n = n/2
            l.append(n)
        else:
            n = n*3 + 1
            l.append(n)
    for i in l:
        if i != 1:
            w = w + str(int(i)) + ","
        else:
            w = w + str(int(i))
    return w
        