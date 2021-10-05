# -*- coding: utf-8 -*-
"""
Write a Python script that given the radius r of a circle by user input, prints the value of its area. Please use round with two decimal places. Consider pi = 3.14159.
"""

pi = 3.14159
r = float(input())

A = pi * r**2
print(round(A,2))
