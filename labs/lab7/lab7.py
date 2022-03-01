"""
Name: Joshua Uys
lab7.py

Bumper

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from random import randint
from graphics import color_rgb, GraphWin, Circle, Point
import time

width = 400
height = 400
radius = 50

win = GraphWin("Bumper", width, height)


def get_random(move_amount):
    random_number = randint(-move_amount, move_amount)
    return random_number

def did_collide(ball1, ball2):
    center1 = ball1.getCenter()
    center2 = ball2.getCenter()

    center1X = center1.getX()
    center1Y = center1.getY()

    center2X = center2.getX()
    center2Y = center2.getY()

    distance_between_circles = (((center1X - center2X) ** 2) + ((center1Y - center2Y) ** 2)) ** 0.5

    if distance_between_circles <= radius * 2:
        return True

def hit_vertical(ball): #, Graphwin win
    center = ball.getCenter()
    centerX = center.getX()
    centerY = center.getY()

    distance_from_left = (((centerX - 0) ** 2) + ((centerY - centerY) ** 2)) ** 0.5
    distance_from_right = (((centerX - width) ** 2) + ((centerY - centerY) ** 2)) ** 0.5

    if distance_from_left <= radius:
        return True

    if distance_from_right <= radius:
        return True

def hit_horizontal(ball): #, Graphwin win
    center = ball.getCenter()
    centerX = center.getX()
    centerY = center.getY()

    distance_from_top = (((centerX - centerX) ** 2) + ((centerY - 0) ** 2)) ** 0.5
    distance_from_bottom = (((centerX - centerX) ** 2) + ((centerY - height) ** 2)) ** 0.5

    if distance_from_top <= radius:
        return True

    if distance_from_bottom <= radius:
        return True

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

def bumper():
    bumper1 = Circle(Point(randint(50,width - 50), randint(50,height - 50)), radius)
    bumper1.setFill(get_random_color())
    bumper1.draw(win)


    bumper2 = Circle(Point(randint(50,width - 50), randint(50,height - 50)), radius)
    # prevents balls starting overlapped
    while did_collide(bumper1, bumper2):
        bumper2 = Circle(Point(randint(50, width - 50), randint(50, height - 50)), radius)
    bumper2.setFill(get_random_color())
    bumper2.draw(win)

    speed = 10

    random_X_number1 = get_random(speed)
    random_X_number2 = get_random(speed)

    random_Y_number1 = get_random(speed)
    random_Y_number2 = get_random(speed)

    while not win.checkMouse():
        bumper1.move(random_X_number1, random_Y_number1)
        bumper2.move(random_X_number2, random_Y_number2)
        time.sleep(0.07)

        did_collide(bumper1, bumper2)

        if did_collide(bumper1, bumper2):
            random_X_number1 *= -1
            random_X_number2 *= -1

            random_Y_number1 *= -1
            random_Y_number2 *= -1

        if hit_horizontal(bumper1):
            random_Y_number1 *= -1

        if hit_horizontal(bumper2):
            random_Y_number2 *= -1

        if hit_vertical(bumper1):
            random_X_number1 *= -1

        if hit_vertical(bumper2):
            random_X_number2 *= -1

bumper()
win.close()