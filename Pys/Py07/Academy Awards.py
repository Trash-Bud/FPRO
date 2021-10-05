# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:32:12 2019

@author: Joana
"""

def academy_awards(alist):
    dict1 = {}
    for i in alist:
        movie = i[1]
        dict1[movie] = dict1.get(movie,0) + 1
    return dict1