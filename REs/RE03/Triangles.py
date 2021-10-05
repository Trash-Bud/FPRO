# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:53:39 2019

@author: Joana
"""

l1 = int(input())
l2 = int(input())
l3 = int(input())

if l1 + l2 < l3 or l1 == 0 or l2 == 0 or l3 == 0:
    print("Not a triangle")
elif l1 == l2 and l2 == l3:
    print("Equilateral")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Isosceles")
elif l1 != l2 and l2 != l3:
    print ("Scalene")
