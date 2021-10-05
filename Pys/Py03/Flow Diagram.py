# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:34:25 2019

@author: Joana
"""

L = int(input())
S = int(input())
R = L

if R > S:
    while R >= S:
        R -= S
    while R != 0:
        L = R
        R = S
        S = L
        while R >= S:
            R -= S
    print(S)

else:
    L = R
    R = S
    S = L
    while R >= S:
        R -= S
    while R != 0:
        L = R
        R = S
        S = L
        while R >= S:
            R -= S
    print(S)    