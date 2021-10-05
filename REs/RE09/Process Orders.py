# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 12:33:16 2019

@author: Joana
"""

def invoice_totals(orders, min):
    f = map(lambda i: tuple([i[0],i[2]*i[3]]) if i[2]*i[3] > min else tuple([i[0],i[2]*i[3] + 10]), orders)
    return list(f)