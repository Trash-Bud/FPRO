# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:33:18 2019

@author: Joana
"""

import math
K = 50
sum_tot = 0
for k in range(0, K + 1):
    sum_divd = math.factorial(4 * k) * (1103 + 26390 * k)
    sum_divs = math.factorial(k) ** 4 * 396 ** (4 * k)
    sum_exp = sum_divd/sum_divs
    sum_tot = sum_tot + sum_exp 
inv_pi = ((2 * math.sqrt(2))/9801) * sum_tot
pi = 1 / inv_pi
pi_round = round(pi, 8)
print(pi_round)