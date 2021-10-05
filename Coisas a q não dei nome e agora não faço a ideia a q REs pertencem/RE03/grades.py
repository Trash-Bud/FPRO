# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:47:56 2019

@author: Joana
"""

def sort_grades(records):
    
    return tuple(sorted(records, key = lambda k: (100 - (sum(list(k[2]))/len(list(k[2]))), k[0], k[1])))
print(sort_grades((('João', 'up20186042', (90, 87)), ('Ana', 'up20186040', (90, 90)), ('José', 'up20186063', (70, 90)), ('Ana', 'up20186061', (90, 90)), ('Tiago', 'up20186070', (100, 90)))))
