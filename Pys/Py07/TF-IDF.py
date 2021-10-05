# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:25:15 2019

@author: Joana
"""
import math
def  tfidf(documents):
    ee = 0
    dict1 = {}
    l = []
    l1 = [] 
    n = 0
    r = []
    n2 = 0
    TF_l = []
    for i in documents:
        l = i.split()
        for s in l: 
            if s.lower() in dict1:
                pass
            else:
                r = []
                TF_l = []
                n = 0
                for e in documents:
                    n2 = 0
                    l1 = e.split()
                    for f2 in l1:
                        if f2.lower() == s.lower():
                            n += 1
                            break
                    for f in l1:
                        if f.lower() == s.lower():
                            n2 += 1
                    TF = n2
                    TF_l.append(TF)
                    if e == documents[len(documents)-1]:
                        IDF = math.log(len(documents)/n)
                        for u in TF_l:
                            r.append(round(IDF * u,3)) 
                dict1[s.lower()] = r
        ee += 1            
    return dict1