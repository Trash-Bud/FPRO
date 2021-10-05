# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:57:14 2020

@author: Joana
"""

d = int(input())
num = int(input())
str_num = str(num)
square = 0
for i in str_num:
    if int(i) > d:
        square += int(i)**2
    else:
        pass
print(square)