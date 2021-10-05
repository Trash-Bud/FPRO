# -*- coding: utf-8 -*-
"""
Write a Python program to help the user arrive in Lisbon at time. Ask the user in how many hours and how many minutes she can spend travelling at most. Return the average velocity (in km/h) that she will need to drive to arrive in time. Assume the distance between Porto and Lisbon is 313 km.

Please round the result.

"""

h = int(input())
min = int(input())

h_t = h + min / 60

v = 313 / h_t

v_round = round(v)

print(v_round)
