"""
Name: Joshua Uys
hw8.py

Problem: Accumulations and conditional control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# nums = [10, 20, 30]
# csv = "10, 20, 30"

from graphics import GraphWin, Circle, Point, Text
import math

def add_ten(nums):
    list_len = len(nums)
    for i in range(list_len):
        nums[i] += 10

# add_ten(nums)

def square_each(list):
    list_len = len(list)
    for i in range(list_len):
        list[i] = list[i] ** 2
    return list

# square_each(nums)

def sum_list(nums):
    accum = 0
    list_len = len(nums)
    for i in range(list_len):
        accum += nums[i]

# sum_list(nums)

def to_numbers(nums):
    list_len = len(nums)
    for i in range(list_len):
        nums[i] = eval(nums[i])

# to_numbers(nums)

def sum_of_square(csv):
    csv_list = csv.split(",")

    for i in range(len(csv_list)):
        csv_list[i] = eval(csv_list[i])

    csv_list_squared = square_each(csv_list)

    accum = 0

    for i in range(len(csv_list_squared)):
        accum += csv_list_squared[i]

    return accum

# sum_of_square(csv)

def starter(weight, wins):

    on_the_team = False

    if weight >= 150:
        if weight <= 160:
            if wins >= 5:
                on_the_team = True

    if weight > 199:
        on_the_team = True

    if wins > 20:
        on_the_team = True

    print(on_the_team)
    return on_the_team

# starter(40, 3)

def leap_year(year):
    is_a_leap_year = False

    if (year / 400) == (year // 400):
        is_a_leap_year = True

    print(is_a_leap_year)
    return is_a_leap_year

# leap_year(2400)

def did_overlap(circle_one, circle_two):
    center_one = circle_one.getCenter()
    center_two = circle_two.getCenter()

    radius_one = circle_one.getRadius()
    radius_two = circle_two.getRadius()

    distance_between_centers = math.sqrt((center_one.getX() - center_two.getX()) ** 2 + (center_one.getY() - center_two.getY()) ** 2)
    both_radii = radius_one + radius_two

    overlap = False

    if distance_between_centers < both_radii:
        overlap = True

    return overlap

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center_one = win.getMouse()
    circumference_point = win.getMouse()
    radius_one = math.sqrt(
        (center_one.getX() - circumference_point.getX()) ** 2 + (center_one.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center_one, radius_one)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_point.getX()) ** 2 + (center_two.getY() - circumference_point.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light blue")
    circle_two.draw(win)

    inst_pt = Point(5, 1.25)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)

    overlap_pt = Point(5, 1)

    overlap_text_display = "The circles do not overlap"

    if did_overlap(circle_one, circle_two) != 0:
        overlap_text_display = "The circles overlap"

    overlap_text = Text(overlap_pt, overlap_text_display)
    overlap_text.draw(win)

    win.getMouse()

# circle_overlap()

if __name__ == '__main__':
    pass
