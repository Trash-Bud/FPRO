# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:34:37 2019

@author: Joana
"""

n1 = int(input())
n2 = int(input())
a = []
for i in range(n1, n2 + 1):
    if i == 2:
        a.append(i)
    for e in range (2, i):
        mod_i = i % e
        if mod_i != 0 and e == i - 1:
            a.append(i)
            break
        elif mod_i != 0:
            pass
        else:
            break
m = ""
for f in range(0, len(a)):
    n_str = str(a[f]) + " "
    m += n_str
print("Prime numbers between", n1, "and", n2, "are:", m)