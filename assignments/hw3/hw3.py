"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def average():
    number_of_grades = eval(input("how many grades do you want to average? "))
    accum = 0
    for i in range(number_of_grades):
        accum += eval(input("enter a grade: "))
    print("Average:", accum/number_of_grades)

def tip_jar():
    tip_accum = 0
    for i in range(5):
        tip_accum += eval(input("How much would you like to tip?"))
    print("Total tips: $", tip_accum)

def newton():
    number_to_square_root = eval(input("Enter the number to square root: "))
    improve = eval(input("How many times do you want to improve? "))
    current_approx = number_to_square_root
    final_approx = 0
    for i in range(improve):
        final_approx = (current_approx + (number_to_square_root/current_approx)) / 2
        current_approx = final_approx
    print("The square root of ", number_to_square_root, "is approximately", final_approx)

def sequence():
    terms = eval(input("How many terms would you like?"))
    sequence_accum = -1
    for i in range(1, terms + 1):
        sequence_accum += 1
        print(sequence_accum + (i % 2), end = " ")

def pi():
    series = eval(input("How many terms in the series?"))
    numerator_accum = -1
    denominator_accum = -1
    subtotal = 1
    for i in range(series + 1 ):
        numerator_accum += 1
        numerator = numerator_accum + (i % 2)
        denominator_accum += 1
        denominator = denominator_accum - (i % 2) + 1
        if (numerator / denominator) != 0:
            subtotal = subtotal * (numerator / denominator)
    result = subtotal * 2
    print("result = ", result)

if __name__ == '__main__':
    pass
