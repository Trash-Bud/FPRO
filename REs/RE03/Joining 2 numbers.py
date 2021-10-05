# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:56:57 2019

@author: Joana
"""

import math
n1 = input()
n2 = input()

if n2 == 0:
    result = 10 * n1
else:
    l_n2 = math.floor(math.log10(n2))+1
    result = (n1 * 10 ** (l_n2)) + n2
print(result)