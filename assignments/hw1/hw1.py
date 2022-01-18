"""
Name: Joshua Uys
BasicCalculator.py


Problem: This program aims to calculate the area and volume using user inputted values as well as converting km to miles, the cost of coffee and the percent of basketball shots made

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the player's total shots: "))
    shots_made = eval(input("Enter how many shots the player made: "))
    shooting_percentage = shots_made / total_shots * 100
    print("Shooting percentage =", shooting_percentage, "%")

def coffee():
    pounds_of_coffee = eval(input("How many pounds of coffee would you like? "))
    cost = pounds_of_coffee * 10.5 + pounds_of_coffee * 0.86 + 1.5
    print("Your total is $", cost)

def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers / 1.61
    print("That's", miles, "miles!")

if __name__ == '__main__':
    pass
