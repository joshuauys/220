"""
Name: Joshua Uys
hw10.py

Loops and Bools

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def fibonacci(n: int):
    fibonacci_list = [0, 1]
    accum = 0

    if n >= 1:
        while accum < n:
            fibonacci_list += [fibonacci_list[accum] + fibonacci_list[accum + 1]]
            accum += 1
        return fibonacci_list[n]
    else: return None

# fibonacci(0)

def interest(principle, rate):
    A = 0
    years = 0

    while A < principle * 2:
        years += 1
        A = principle * (1 + rate) ** years

    return years
# interest(100, 0.20)

def syracuse(n: int):
    current_number = n
    current_number_even: Bool

    if current_number % 2 == 0:
        current_number_even = True
        print("Even")
    if current_number % 2 == 1:
        current_number_even = False
        print("Odd")

    while current_number != 1:
        if current_number_even:
            current_number = current_number / 2
            print("even")
        elif current_number_even == False:
            current_number = (3 * current_number) + 1
            print("odd")

        print(current_number)

# syracuse(15)

def goldbach(n: int):
    def is_prime(x):
        is_prime = True
        n_range = []
        n_range_remainders = []

        for i in range(2, x):
            n_range.append(i)

        for i in n_range:
            n_range_remainders.append(x % i)

        for i in range(len(n_range_remainders)):
            if n_range_remainders[i] == 0:
                is_prime = False
        return is_prime

    def is_even(y):
        if y % 2 == 0:
            return True
        elif y % 2 == 1:
            return False

    def find_two_numbers(sum, list):
        for x in range(len(list)):
            for i in list:
                if i + list[x] == sum:
                    print(i, x, "two numbers")


    print("even: ", is_even(n))
    print("prime: ", is_prime(n))


# goldbach(13)

from face import Face
from graphics import Point, GraphWin

width = 800
height = 800
win = GraphWin("3 Door Game", width, height)

face = Face(win, Point(400, 400), 200)
face.shock()

win.getMouse()
win.close()


