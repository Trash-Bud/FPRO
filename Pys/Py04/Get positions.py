# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:37:15 2019

@author: Joana
"""

def get_positions(sentence, word_list):
    sentence = sentence.split(" ")
    l = []
    if sentence[0] == sentence[1]:
        for e in range(len(word_list)):
            if sentence[0] == word_list[e]:
                l.append(str(e))
    else:
        for i in sentence:
            for e in range(len(word_list)):
                if i == word_list[e] :
                    l.append(str(e))
    w = ""

    if len(l) == 0 or len(l) == 1:
        return w
    else:
        w = l[0] + " " + l[1]
        return w