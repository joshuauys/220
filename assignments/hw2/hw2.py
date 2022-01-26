"""
Name: Joshua Uys
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    print(list(range(3, upper_bound, 3)))

# sum_of_threes()

def multiplication_table():
    step = 0
    for i in range(1, 11):
        for x in range(1, 10):
            print((i * x), end = "\t")
        print("\n")

# multiplication_table()

def triangle_area():
    side_a = eval(input("Enter side a length"))
    side_b = eval(input("Enter side b length"))
    side_c = eval(input("Enter side c length"))

    s = (side_a + side_b + side_c) / 2
    area = (s*(s-side_a)*(s - side_b)*(s-side_c)) ** 0.5
    print("area of the triangle = ", area)

# triangle_area()

def sum_squares():
    pass


def power():
    pass


if __name__ == '__main__':
    pass
