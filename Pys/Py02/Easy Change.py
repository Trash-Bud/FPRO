# -*- coding: utf-8 -*-
"""
You're helping a teller decide how to give change. Write a Python script that given the price of the sale and the amount received by user input, then prints a string indicating how many notes of each amount they have to give as change. Consider that the largest note available is the 50€ note and that all prices and amounts received are multiples of 5 (no coins!).

The result should be a string with the number of notes of each amount, separated by a space: "#50 #20 #10 #5".

Hint: To help format the result, use type conversions to string.
"""

price = float(input())
received = float(input())


def easy_change(price, received):
    change = int(received) - int(price)
    c5 = change / 5
    c10 = change / 10
    c20 = change / 20
    c50 = change / 50
    n50 = "0 "
    n20 = "0 "
    n10 = "0 "
    n5 = "0 "

    if change <= 5:
        n5 = str(round(c5)) + " "
    elif 10 <= change < 20 and change%10 == 0:
        n10 = str(c10) + " "
    elif 10 <= change < 20 and change%10 != 0:
        n10 = str(round((change - 5)/10)) + " "
        n5 = "1"
    elif 20 <= change < 50 and change%20 == 0:
        n20 = str(round(c20)) + " "
    elif 20 <= change < 50 and change%20 != 0:
        t5 = (change - 5)
        t15 = (change - 15)
        if t5%20 == 0:
            n20 = str(t5/20) + " "
            n5 = "1 "
        if t15%20 == 0:
            n20 = str(t15/20) + " "
            n5 = "1 "
            n10 = "1 "
        else:
            n20 = str(round((change - 10) / 20)) + " "
            n10 = "1 "
    elif 50 <= change and change%50 == 0:
        n50 = str(round(c50)) + " "
    elif 50 <= change and change%50 != 0:
        t5 = (change - 5)
        t10 = (change - 10)
        t20 = (change - 20)
        t15 = (change - 15)
        t30 = (change - 30)
        t25 = (change - 25)
        t35 = (change - 35)
        t40 = (change - 40)
        if t5%50 == 0:
            n50 = str(round(t5/50)) + " "
            n5 = "1 "
        elif t10%50 == 0:
            n50 = str(round(t10/50)) + " "
            n10 = "1 "
        elif t20%50 == 0:
            n50 = str(round(t20 / 50)) + " "
            n20 = "1 "
        elif t15%50 == 0:
            n50 = str(round(t15 / 50)) + " "
            n10 = "1 "
            n5 = "1 "
        elif t30%50 == 0:
            n50 = str(round(t30 / 50)) + " "
            n10 = "1 "
            n20 = "1 "
        elif t25%50 == 0:
            n50 = str(round(t25 / 50)) + " "
            n20 = "1 "
            n5 = "1 "
        elif t35%50 == 0:
            n50 = str(round(t35 / 50)) + " "
            n10 = "1 "
            n5 = "1 "
            n20 = "1 "
        elif t40%50 == 0:
            n50 = str(round(t40 / 50)) + " "
            n20 = "2 "
        else:
            n50 = str(round((change-45)/50))
            n20 = "2 "
            n5 = "1 "
    return print(n50 + n20 + n10 + n5)

easy_change(price, received)
