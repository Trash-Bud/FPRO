# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:56:41 2020

@author: Joana
"""

import math
num = int(input())
l = []
n = 0
if num == 0:
    print(0)
else:
    for i in range(0, int(math.log10(num) + 1 )):
        l.append(int(num / 10 ** i) - int(num / 10 ** (i + 1))* 10)
    for i in range(0, len(l)):
        n = n + l[int(len(l) - 1 - i)] * 10 ** i

    print (n)
    