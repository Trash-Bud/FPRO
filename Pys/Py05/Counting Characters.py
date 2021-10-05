# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:40:05 2019

@author: Joana
"""

import string
def count_chars(astring):
    l_alph = list(string.ascii_letters)
    l_char = list(string.punctuation)
    l = []
    count_alph = 0
    count_char = 0
    count_num = 0
    for i in astring:
        if i in l_alph:
            count_alph += 1
        elif i in l_char:
            count_char += 1
        else:
            count_num += 1
    l.append(count_alph)
    l.append(count_num)
    l.append(count_char)
    return tuple(l)