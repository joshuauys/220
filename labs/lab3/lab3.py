"""
Name: Joshua Uys
traffic

Problem: Calculate statistics for the Department of Traffic

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def traffic():
    roads_count = eval(input("How many roads were surveyed?"))
    cars_total_accum = 0
    for x in range(roads_count):
        print("How many days was road", (x + 1), "surveyed?")
        days_count = eval(input())
        cars_average_accum = 0
        for i in range(days_count):
            print("How many cars travelled on day", (i + 1), "?")
            cars_average_accum += eval(input())
        average = cars_average_accum / days_count
        cars_total_accum += cars_average_accum
        print("Road" , x + 1, "average vehicles per day: ", round(average, 2))
    print("Total number of vehicles travelled on all roads: ", cars_total_accum)
    print("Average number of vehicles per road", round(cars_total_accum / roads_count, 2))