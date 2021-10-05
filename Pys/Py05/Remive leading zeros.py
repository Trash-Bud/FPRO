# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:43:37 2019

@author: Joana
"""

def remove_leading(ip):
    ip = ip.split(".")
    w = ""
    for i in range(len(ip)):
        ip[i] = int(ip[i])
        ip[i] = str(ip[i])
    for i in range(len(ip)):
        if i == len(ip)-1:
            w = w + ip[i]
        else:
            w = w + ip[i] + "."
    return w
