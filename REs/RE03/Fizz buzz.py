# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:56:40 2019

@author: Joana
"""

n = int(input())
for i in range(1, n+1):
    mod_3 = i % 3
    mod_5 = i % 5
    if mod_3 == 0 and mod_5 == 0:
        pass
    elif mod_3 == 0:
        print ("Fizz", end = " ")
    elif mod_5 == 0:
        print("Buzz", end = " ")
    else:
        print(str(i), end = " ")