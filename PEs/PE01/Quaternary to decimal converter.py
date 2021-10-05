# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:59:29 2020

@author: Joana
"""

quat = int(input())
str_quat = str(quat)
d = 0
l =[]

for i in str_quat:
    l.append(i)
for i in range(0, len(l)):
    d = d + (int(l[len(l) - 1 - i]) * 4 ** int(i))

print(d)