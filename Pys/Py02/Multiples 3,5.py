# -*- coding: utf-8 -*-
"""
Define a function sum_multiples(n) that returns the sum of all the natural numbers that are a multiple of 3 or 5 up until n (inclusive).

def sum_multiples(n):
    # my code here
    return # FIXME
The sum of all natural numbers up to n can be calculated using the formula:


For example, the sum of all numbers up to 5 is 1 + 2 + 3 + 4 + 5 = 15 , or using the formula:
"""

def sum_multiples(n):
    n_Sum = 0
    for n1 in range (0, n + 1):
        if n1%3 == 0 or n1%5 == 0:
            n_Sum = n1 + n_Sum
        else:
            pass
    return (n_Sum)
