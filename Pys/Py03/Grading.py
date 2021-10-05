# -*- coding: utf-8 -*-
"""
Write a Python program that, given the four components of the FPRO grade, by user input, returns the student's grade, an integer from 0 to 20, by using the formula:

grade = (LE + RE + 5 * PE + 3 * TE) / 50

The program returns:

"Input error", if the any of the components is not between 0 and 100
"RFC", if the PE < 40 or the TE < 40
the grade as an integer, otherwise
"""

import math
Le = int(input())
Re = int(input())
Pe = int(input())
Te = int(input())

if Le < 0 or Le > 100 or Re < 0 or Re > 100 or Pe < 0 or Pe > 100 or Te < 0 or Te > 100:
    print("Input error")

elif Pe < 40 or Te < 40:
    print("RFC")

else:
    g = (Le + Re + 5 * Pe + 3 * Te) / 50 + 0.5
    print(int(g))
