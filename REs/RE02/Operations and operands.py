# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:52:33 2019

@author: Joana
"""

Pay = input()
TIME = 2
Freq = input()
RealI = input()

FinalA = Pay * (1 + RealI/ Freq)**(Freq * TIME)

print (round(FinalA, 3))