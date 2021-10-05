# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:14:29 2019

@author: Joana
"""
def find_dtype(atuple, data_type):
    l = []
    for i in atuple:
        t_str = str(type(i))
        print(t_str)
        if data_type not in t_str:
            pass
        else:
            l.append(i)
    return tuple(l)

 
print(find_dtype((1, False, 'hello', 2.0, 'world'), "str"))
