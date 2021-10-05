# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 11:49:53 2019

@author: Joana
"""
astring = str(input())


def palindrome(astring):
    count = 0
    for i in range(0, len(astring)):
        w = ""
        for e in range(i + 1, len(astring)):
            if astring[i] == astring[e]:
                w = astring[i:(e+1)]
                if i == e - 1 or i == e - 2:
                    count += 1
                else:
                    if w == w[::-1]:
                        count += 1
                    else:
                        pass
            else:
                pass
    return ("The string '{}' contains {} palindrome substrings.".format(astring, count))


print(palindrome(astring))
