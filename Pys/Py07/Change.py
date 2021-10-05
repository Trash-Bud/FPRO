# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:33:59 2019

@author: Joana
"""

def change(money):
   dict1 = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
   
   for i in dict1:
       while round(money,2) >= round(i,2):
           money -= i
           dict1[i] += 1
   return dict1          