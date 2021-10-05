# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:44:13 2020

@author: Joana
"""

integers = input()
reals = input()

if integers == [] or reals == []:
    pass
else:
    for i in range(0, len(integers)):
        
        if float(integers[i]) > float(reals[i]):
            print(integers[i], end = " ")

        elif float(integers[i]) < float(reals[i]):
            print(reals[i], end = " ") 

        elif float(integers[i]) == float(reals[i]):
            print(integers[i], end = " ")   