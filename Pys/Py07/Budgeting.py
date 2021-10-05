# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:35:11 2019

@author: Joana
"""

def budgeting(budget, products, wishlist):
    total = 0
    p_ord = {}
    for i in wishlist:
        total += wishlist[i] * products[i]
    if total < budget:
        return wishlist
    else:
        p_list = sorted(products.items())
        p_list.sort( key = lambda k: (k[1]))
        for l in p_list:
            p_ord[l[0]] = l[1]
        for f in p_ord:
            if total <= budget:
                break
            if f in wishlist:
                while total > budget and wishlist[f]!= 0:
                    total -= p_ord[f]
                    wishlist[f] -= 1
                if wishlist[f] == 0:
                    del wishlist[f]
        
    return wishlist

