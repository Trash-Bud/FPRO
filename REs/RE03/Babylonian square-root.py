# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:57:18 2019

@author: Joana
"""

import random
num = int(input())

x0 = random.randint(1,num)
x1 = (x0 + num/x0)/2

i = 5
while i != 0:
    x1 = (x0 + num/x0)/2
    i = round((int(x1) - x1), 2) - round((int(x0) - x0), 2)
    x0 = x1

print(round(x0, 2))
