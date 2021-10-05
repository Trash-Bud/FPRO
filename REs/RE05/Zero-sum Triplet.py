# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:04:32 2020

@author: Joana
"""

def triplet(atuple):
    l =[]
    sum2 = 0
    sum3 = 1
    for i in range(0, len(atuple)-2):
        sum1 = atuple[i]
        if sum3 == 0:
            break
        for e in range(i+1,len(atuple)):
            sum2 = sum1 + atuple[e]
            if sum3 == 0:
                break
            for f in range(e+1,len(atuple)):
                sum3 = 0
                sum3 = sum2 + atuple[f]
                if sum3 == 0:
                    l.append(atuple[i])
                    l.append(atuple[e])
                    l.append(atuple[f])
                    break
                else:
                    pass
    return tuple(l)