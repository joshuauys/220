"""
Name: Joshua Uys
hw11.py

Sales Person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(file_name):
        file = open(file_name, "r")
        text = file.read()

        lines = text.split("\n")
        sales_people = lines


    def quota_report(quota):
        entries = []

        num_lines = len(self.sales_people)
        print(sales_people)
        print(num_lines)


        for i in range(num_lines):
            entries.append(str(lines[i]).split(","))

SalesForce.add_data("sales_data.txt")
SalesForce.quota_report(9)

