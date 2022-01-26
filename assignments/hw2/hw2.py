"""
Name: Joshua Uys
<ProgramName>.py

Problem: Solve basic math problems

Certification of Authenticity:

I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    accum = 0

    for i in range(1, (upper_bound - upper_bound % 3) // 3 + 1):
        print(list(range(3, upper_bound, 3)))
        accum += 3 * i
        print("accum:" , accum)

def multiplication_table():
    for i in range(1, 11):
        for i_2 in range(1, 10):
            print((i * i_2), end = "\t")
        print("\n")

def triangle_area():
    side_a = eval(input("Enter side a length"))
    side_b = eval(input("Enter side b length"))
    side_c = eval(input("Enter side c length"))

    s = (side_a + side_b + side_c) / 2
    area = math.sqrt((s*(s-side_a)*(s - side_b)*(s-side_c)))
    print("area of the triangle = ", area)

def sum_squares():
    upper_range = eval(input("Enter the upper range: "))
    lower_range = eval(input("Enter the lower range: "))
    acc = 0

    for i in range(lower_range, upper_range + 1):
        acc = acc + (i ** 2)

    print("Square sum: ", acc)

def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    result = base

    for i in range(exponent - 1):
        print("result:" , result)
        result = result * base

    print(base, "^", exponent, "=", result)

if __name__ == '__main__':
    pass
