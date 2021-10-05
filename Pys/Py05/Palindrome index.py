# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:42:59 2019

@author: Joana
"""

def palindrome_index(s):
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            s2 = []
            w = ""
            for e in s:
                s2.append(e)
            s2[i] = ""
            for f in s2:
                if f != "":
                    w += f
            if w == w[::-1]:
                return i
            elif i == len(s) - 1:
                return -1
            else:
                continue
            