# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:40:54 2019

@author: Joana
"""
def batch_norm(alist, batch_size):
    for i in range(0, len(alist), batch_size):
        batch = alist[i:i+batch_size]
        m = batch.copy()
        m = sorted(m)
        m = m[(len(m)-1)//2:(len(m)//2) + 1]
        median = sum(m)/len(m)
        yield [x - median for x in batch]
        
print(list(batch_norm(    [-1, 0, 1, 1, 2, 4], 3)))