# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:34:20 2019

@author: Joana
"""

def biggest_member(atuple):
    if atuple == ():
        return ()
    if type(atuple[0]) is tuple:
        if len(biggest_member(atuple[0])) > len(biggest_member(atuple[1::])):
            return biggest_member(atuple[0])
        else:
            return biggest_member(atuple[1::])
    elif type(atuple[0]) is not tuple:
        if len(atuple) >= len(biggest_member(atuple[1::])):
            return atuple
        else:
            return biggest_member(atuple[1::])
print( biggest_member(    ((6, (10, 20, 5, 7, 50, 10, 70, -2), 8, 9, 10, 11), 5, (2, 3, 1))))