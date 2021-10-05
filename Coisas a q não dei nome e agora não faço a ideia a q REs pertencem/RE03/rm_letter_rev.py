# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:12:41 2019

@author: Joana
"""
la = input()
astr = input()
def rm_letter_rev(l, astr):
    str1= ""
    for i in range(len(astr)):
        if astr[i] == l:
            pass     
        else:
            str1 = str1 + astr[i]
    return str1[::-1]

print(rm_letter_rev(la,astr))