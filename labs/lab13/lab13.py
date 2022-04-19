"""
Name: Joshua Uys

lab13.py

List Searching

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import algorithms.py

def trade_alert(filename):
    text = open(filename, "r").read()
    stock_list = text.split(" ")
    stock_list_len = len(stock_list)
    for i in range(stock_list_len):
        if int(stock_list[i]) >= 500 and int(stock_list[i]) < 830:
            print("Pay attention, at", i + 1, "seconds pased the hour \n stock volume exceeded 500")
        if int(stock_list[i]) >= 830:
            print("Warning, at", i + 1, "seconds passed the hour \n stock volume exceeded 830")

trade_alert("trades.txt")