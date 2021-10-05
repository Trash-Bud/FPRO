# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:48:32 2019

@author: Joana
"""

def anagram(alist):
    letters_low = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letters_up = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    l1 = []
    l2 = []
    l3 = []
    la = []
    for e in alist:
        l1.append(e)
        for i in e:
            if i in letters_up:
                i = letters_low[letters_up.index[i]]
                l2.append(i)
            elif i in letters_low:
                l2.append(i)
            else:
                pass
        l2.sort()
        for f in alist[e+1::]:
            for s in f:
                if s in letters_up:
                    s = letters_low[letters_up.index[s]]
                    l3.append(s)
                elif s in letters_low:
                    l3.append(s)
                else:
                    pass
            l3.sort()
            if l2 == l3:
                l1.append(f)
            else:
                pass
        la.append(l1)
    return la
        
print(anagrams(['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']))
        