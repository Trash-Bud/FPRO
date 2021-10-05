# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:51:42 2019

@author: Joana
"""

tag = input()
text = input()

def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)

print (add_tags(tag, text))