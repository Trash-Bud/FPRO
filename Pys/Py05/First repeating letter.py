# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:42:05 2019

@author: Joana
"""

def repeated_letter(s):
    for i in s:
        for e in range(s.index(i)+1, len(s)):
            if i == s[e]:
                return i