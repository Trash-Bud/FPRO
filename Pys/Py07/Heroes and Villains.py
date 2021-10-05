# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 18:03:38 2019

@author: Joana
"""

def fight(heroes, villain):
    for hero in heroes:
        if hero["category"] == villain["category"]:
            if hero["health"] >= villain["health"]:
                hero["score"] += 1
                return "{} defeated the villain and now has a score of {}".format(hero["name"], hero["score"])
            else:
                villain["health"] = villain["health"] - hero["health"]/2
        else:
            pass
    return "{} prevailed with {}HP left".format(villain["name"], round(villain["health"],1))        
