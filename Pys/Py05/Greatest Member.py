# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:44:07 2019

@author: Joana
"""

def greatest_member(atuple):
    l =["a"]
    l1=[0]
    w = 0
    for i in atuple:
        w = 0
        if type(i) is tuple:
            for e in i:
                if type(e) is tuple:
                   for f in e:
                        for h in f:
                            w = w + ord(h)
                else:
                    for f in e:
                        w = w + ord(f)
            if w > l1[0]:
                l[0] = i
                l1[0] = w
        else:
            for e in i:
                w = w + ord(e)
            if w > l1[0]:
                l[0] = i
                l1[0] = w
    return l[0]

                    