# -*- coding: utf-8 -*-
"""
You are budgeting for a car trip and need to know how much you will spend in fuel. Define a function trip_cost(distance, litres_100km, price) that given the distance to travel, distance, the number of litres of fuel needed to travel 100 km as litres_100km and the price (per litre) of fuel as price, returns the total cost of fuel for the trip. Use round with 2 decimal places.

def trip_cost(distance, litres_100km, price) 
    #my code here
    return  # FIXME

"""
#distance = float(input())
#litres_100km = float(input())
#price = float(input())

def trip_cost(distance, litres_100km, price):
    total = distance * litres_100km / 100 * price
    return round(total, 2)

#print(trip_cost(distance, litres_100km, price))