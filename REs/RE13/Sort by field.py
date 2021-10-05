# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 12:33:27 2020

@author: Joana
"""

def sort_by_field(filename, field):
    l = []
    w = ""
    file = open(filename,"r")
    file = file.read()
    file = file.split("\n")
    r = 0
    for i in file:
        i1 = i.split(",")
        file[r] = i1
        r += 1
    for s in file[0]:
        l.append(s)
    sorted(file, key = lambda x: (x[l.index(field)]))
    for i in file:
        for e in i:
            if e == i[len(i)-1]:
                w += e
            else:
                w += e + ","
        w += "\n"
    return w