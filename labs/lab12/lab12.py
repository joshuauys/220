"""
Name: Joshua Uys

lab12.py

Loops and Lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint

# scores = [75, 90, 82]

def find_and_remove_first(list, value):
    position_in_list = 0
    while list[position_in_list] != value:
        position_in_list += 1

    list.insert(position_in_list, "Joshua")
    list.pop(position_in_list + 1)

# find_and_remove_first(scores, 75)

def good_input():
    user_input = eval(input("Enter a value between 1 and 10"))
    good = False

    while not good:
        if user_input < 1:
            print("\n")
            print("That value is too small")
            user_input = eval(input("Enter a value between 1 and 10"))
        elif user_input > 10:
            print("\n")
            print("That value is too big")
            user_input = eval(input("Enter a value between 1 and 10"))
        else: print("\n"); print("good value"); good = True; return user_input


# good_input()

def num_digits():
    user_input = eval(input("Enter a value"))
    while user_input > 0:
        digits = 0
        division = None
        while division != 0:
            division = user_input // 10
            digits += 1
        print(digits)
        # user_input = eval(input("Enter a value"))

# num_digits()
# INCOMPLETE ^

def hi_lo_game():
    number_of_guesses = 7
    random_number = randint(1, 100)
    guessed = False
    while number_of_guesses > 0 and guessed == False:
        number_of_guesses -= 1
        user_input = eval(input("Guess a value between 1 and 100"))

        if user_input > random_number:
            print("too high")
            print("\n")

        if user_input < random_number:
            print("too low")
            print("\n")

        if user_input == random_number:
            guessed = True
            print("correct")
            print("You win in", 7 - number_of_guesses, "guesses!")
        elif number_of_guesses == 0:
            print("you lose, the number was", random_number)

# hi_lo_game()



