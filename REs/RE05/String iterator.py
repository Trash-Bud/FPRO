# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:59:55 2020

@author: Joana
"""

def rm_letter_rev(l, astr):
    str1= ""
    for i in range(len(astr)):
        if astr[i] == l:
            pass     
        else:
            str1 = str1 + astr[i]
    return str1[::-1]
