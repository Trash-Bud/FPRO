# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:20:30 2019

@author: Joana
"""
import string
def exactly(s):
    l = []
    n_l = []
    s_l = []
    qm_count = 0
    p_count = 0
    for i in s:
        if i == "?" or i in string.digits:
            l.append(i)
    for e in l:
        if len(n_l) != 0:
            break
        else:
            for f in l:
                if e != "?" and f != "?":
                    p_count = 0
                    p_count = int(e) + int(f)
                    if p_count == 10:
                        for s in range(l.index(f), l.index(e)):
                            if s == "?":
                                qm_count += 1
                            if qm_count != 3:
                                n_l.append(f + e)
                                break
                            else:
                                s_l.append(f + e)
                                qm_count = 0
    if len(n_l) != 0:
        return "The sequence {} is OK with the pairs: {}".format(s, tuple(n_l)) 
    else:
        return "The sequence {} is OK with the pairs: {}".format(s, tuple(s_l))

print(exactly('acc?7??sss?3rr1??????5???5'))