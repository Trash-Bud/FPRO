# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:44:30 2019

@author: Joana
"""

def summary_ranges(astring):
    astring = astring.split(",")
    w = ""
    for i in range(len(astring)):
        if i == len(astring)-1:
            if int(astring[i]) - 1 == int(astring[i - 1]):
                w = w + "->" + str(astring[i])
            else:
                w = w + str(astring[i])
        elif int(astring[i]) + 1 == int(astring[i + 1]) and int(astring[i]) - 1 != int(astring[i - 1]):
            w = w + str(astring[i])
        elif int(astring[i]) + 1 == int(astring[i + 1]):
             pass      
        elif int(astring[i]) - 1 == int(astring[i - 1]):
            w = w + "->" + str(astring[i]) + ","

        else:
            w = w + str(astring[i]) + ","

    return w