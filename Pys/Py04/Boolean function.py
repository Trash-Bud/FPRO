# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:35:27 2019

@author: Joana
"""

def validate(n):
    return (( "int" in str(type(n))  or "float" in str(type(n))) and n>=0 and n<=100)