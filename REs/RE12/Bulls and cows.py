# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:38:06 2019

@author: Joana
"""

import random
def bulls_cows(seed):
    r = random.Random(seed)
    n = str(r.randrange(0, 10000))
    
    if len(n) == 3:
        n = "0" + n
    elif len(n) == 2:
        n = "00" + n
    elif len(n) == 1:
        n = "000" + n
    
    n = [i for i in n]

    def closure(guess):
        guess_ = [i for i in str(guess)]
        cows = 0
        bulls = 0
        counted = []
        for i in range(0, 4):
            if n[i] == guess_[i]:
                cows += 1
                guess_[i] = "X"
                n[i] = "X"
        for i in range(0, 4):
            if guess_[i] == "X":
                continue
            if guess_[i] in n:
                bulls += 1
                guess_[i] = "X"
                n[i] = "X"
        return (cows, bulls)
    return closure