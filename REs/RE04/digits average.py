# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:56:12 2020

@author: Joana
"""

import math
def digits_average(n): 
    if n == 0 or int(math.log10(n) + 1) == 1: #if n = 0 or n has 1 digit the mean is the number itself
        n1 = n
    else:
        while math.ceil(int(math.log10(n) + 1)) != 1: #as long as our result has more than one digit
            num = 0 # it's going to be incremeanted to obtain the average and needs to be reseted after each loop
            for v in range(0, int(math.log10(n) + 1)): #for v between 0 and the length of n
                n1 = abs(int(n / 10 ** (v)) - 10 * int(n /10 ** (v + 1))) #calculates digit of lower index
                    #ex.: for v = 0 and n = abc --> int(abc / 10 ** 0) - 10 * int(abc / 10 ** 1) = int(abc) - 10 * int(ab,c) = abc - 10 * ab = abc - ab0 = c  
                n2 = abs(int(n / 10 ** (v + 1)) - 10 * int(n /10 ** (v + 2))) #calculates digit of lower index + 1
                if n2 == 0: #stops the loop when the end of the number is reached 
                    break
                else:
                    average = math.ceil((n1 + n2)/2) # calculates the average between n1 and n2
                    num = num + average * 10 ** v #makes the averages in qa single number
            n = num # makes n into the num to repeat the cycle
    return n
