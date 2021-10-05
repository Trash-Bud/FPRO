# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:20:11 2019

@author: Joana
"""

n = int(input())
str_n = str(n)
if n < 10:
    print('Looping number')
else:
    for i in range(len(str_n)-1):
        if abs(int(str_n[i]) - int(str_n[i+1])) != 1:
            if abs(int(str_n[i]) - int(str_n[i+1])) == 9:
                if i == len(str_n) - 2:
                    print('Looping number')
                    break   
                else:
                    pass
            else:
                print('Not a looping number')
                break
        else:
            if i == len(str_n) - 2:
                print('Looping number')
                break