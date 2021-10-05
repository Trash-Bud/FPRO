# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:58:41 2020

@author: Joana
"""

tS = float(input())
tC = float(input())
tR = float(input())

if tS > 4 or tC > 4 or tR > 4:
    print("Time")
elif tS > 0.75:
    print("Swimming")
elif tC > 2:
    print("Cycling")
elif tR > 1.25:
    print("Running")
else:
    print(tS + tC + tR)