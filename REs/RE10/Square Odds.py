# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:15:10 2019

@author: Joana
"""

def square_odds(values):
    if type(values) is str:
        values = values.split(",")
    if len(values) == 1:
        if int(values[0]) % 2 != 0:
            return str((int(values[0]))**2)
        else:
            return ""
    elif int(values[0]) % 2 != 0:
        return str(int(values[0])**2) + "," + square_odds(values[1::])
    else:
        return square_odds(values[1::])
