"""
Joshua Uys
lab1.py

Interest calculator

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

annual_interest_rate = eval(input("What is your annual interest rate?"))
days_in_billing_cycle = eval(input("How many days are in your billing cycle?"))
net_balance = eval(input("What is your previous net balance?"))
payment_amount = eval(input("What is your payment amount?"))
payment_day = eval(input("What day in your billing cycle was a payment made?"))

average_daily_balance = ((net_balance * days_in_billing_cycle) - (payment_amount * (days_in_billing_cycle - payment_day))) / days_in_billing_cycle

monthly_interest_rate = annual_interest_rate / 100 / 12
monthly_interest_charge = average_daily_balance * monthly_interest_rate

print("Your monthly interest charge is $", round(monthly_interest_charge,2))