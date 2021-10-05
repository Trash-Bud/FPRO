# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 08:53:57 2019

@author: Joana
"""

def local_minima(alist, n):
    l1 = []
    l2 = []
    l3 = []
    fail = []
    t = int(n/2)
    for e in range(len(alist)):
        if e - t < 0 or e + t > len(alist) - 1:
            for y in range(t + 1):
                if e - y < 0:
                    for f in range(y):
                        l1.append(alist[e-f])
                    for r in range(t + 1):
                        l1.append(alist[e+r])
                    break
                elif e + y > len(alist) - 1:
                    for f in range(t + 1):
                        l1.append(alist[e-f])
                    for r in range(y):
                        l1.append(alist[e+r])
                    break
                else: pass

        elif e-1 >= 0 and e + 1 <= len(alist) - 1:
            for r in range(t + 1):
                l1.append(alist[e-r])
                l1.append(alist[e+r])
        l2 = l1
        l1.sort()
        l3 = [l1[0],e + l2.index(l1[0])]
        if tuple(l3) in fail:
            pass
        if tuple([l1[0],e + l2.index(l1[0]) - 1]) in fail or tuple([l1[0],e + l2.index(l1[0]) + 1]) in fail:
            pass
        else:
            fail.append(tuple(l3))
        l1 = []            
    return f

print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))