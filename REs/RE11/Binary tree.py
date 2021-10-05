# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:08:23 2019

@author: Joana
"""

def binary_tree(key, tree):
    if tree[0] == key:
        return tree[1]
    elif key < tree[0]:
        return binary_tree(key,tree[2]())
    else:
        return binary_tree(key, tree[3]())
    