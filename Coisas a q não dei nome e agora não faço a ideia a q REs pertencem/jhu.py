# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 10:51:05 2019

@author: Joana
"""


def summary_ranges(astring):
    astring = astring.split(",")
    l = [astring[0]]
    i = int(astring[0])
    w = ""
    while i != len(astring) - 1:
        if int(astring[i]) + 1 == int(astring[i + 1]):
            l.append("->")
            i = i + 1
        else:
            if astring[i] in l:
                l.append(astring[i+1])    
            else:
                l.append(astring[i])
                l.append(astring[i+1])
            i= i +1
    l.append(astring[len(astring) -1])
    i = 0
    while i < (len(l) - 1):
        if l[i] =="->":
            while l[i] == "->":
                i += 1
            w = w + "->" + l[i] + ","
            i += 1
        else:
            w = w + l[i]
            if i == len(l)-1:
                break
            elif l[i+1] != "->":
                w += ","
            i += 1
            
    return w
        
print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))