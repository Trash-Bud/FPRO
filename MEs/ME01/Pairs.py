# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:43:26 2020

@author: Joana
"""

n = str(input())
n1 = 0
n2 = 0
count = 0

for i in range(0, len(n)):
    if i == len(n) - 1:
        break
    else:
        n1 = int(n[i]) + int(n[i + 1])
        div = n1 / 2
        if div == int(n[i]):
            count += 1
        else:
            pass

print(count)