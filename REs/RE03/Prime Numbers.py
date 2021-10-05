# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:56:15 2019

@author: Joana
"""

num = int(input())

if num == 2:
    print("True")
elif num == 1:
    print("False")
else:
    for n in range(2,num):
        if (num % n) == 0:
            print("False")
            break
        elif n == num - 1:
            print("True")
            break