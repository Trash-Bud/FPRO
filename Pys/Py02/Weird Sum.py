# -*- coding: utf-8 -*-
"""
Write a Python script that given two integers a and b, prints the value of their sum. However, if the difference of a and b is an even number, the value of the sum is doubled, on the other hand, if the difference is an odd number, the value of the product of a and b gets added to the value of the sum.

Do not use conditionals (e.g. if).
"""

a = float(input())
b = float(input())

d = a - b
is_odd = d % 2
is_even = 1 - is_odd
e = (a + b) + is_even * (a + b) + is_odd * (a * b) 
print(round(e))
