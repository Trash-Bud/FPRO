# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:29:47 2019

@author: Joana
"""

def mult(M,N):
    s = 0
    f1 = 0
    f2 = -1
    l =[]
    f = []
    for e in M:
        f1 = 0
        f2 = 0
        for y in range(len(M)):
            for i in N:
                if len(i) != len(M):
                    return f
                else:
                    s += i[f2] * e[f1]
                    f1 += 1
                    if f1%len(i) == 0 and f1 != 0:
                        l.append(s)
                        s = 0
                        f1 = 0
        f.append(l)
        l = []
    return f
print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
    