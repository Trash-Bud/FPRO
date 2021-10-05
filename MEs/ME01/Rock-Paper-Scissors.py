# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:44:35 2020

@author: Joana
"""

A = str(input())
B = str(input())
a = ["rock", "paper", "scissors"]

if A == a[0] and B == a[0]:
    print("That's a draw")
elif A == a[0] and B == a[1]:
    print("The winner is B")
elif A == a[0] and B == a[2]:
    print("The winner is A")
elif A == a[1] and B == a[0]:
    print("The winner is A")
elif A == a[1] and B == a[1]:
    print("That's a draw")
elif A == a[1] and B == a[2]:
    print("The winner is A")
elif A == a[2] and B == a[0]:
    print("The winner is B")
elif A == a[2] and B == a[1]:
    print("The winner is A")
elif A == a[2] and B == a[2]:
    print("That's a draw")
