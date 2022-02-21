"""
Name: Joshua Uys
lab5.py

Graphics, strings and lists

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Point, GraphWin, Text, Polygon, Circle, color_rgb, Entry
import math

width = 800
height = 400

def triangle():
    win = GraphWin("Triangle", width, height)

    instruction_point = Point(width / 2, height - 50)
    instructions = Text(instruction_point, "Click three times, one for each point of your triangle")
    instructions.draw(win)

    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()

    # calculate side lengths
    side_a = math.sqrt((point1.getX()-point2.getX()) ** 2 + (point1.getY()-point2.getY()) ** 2)
    side_b = math.sqrt((point2.getX()-point3.getX()) ** 2 + (point2.getY()-point3.getY()) ** 2)
    side_c = math.sqrt((point3.getX()-point1.getX()) ** 2 + (point3.getY()-point1.getY()) ** 2)

    # calculate perimeter
    perimeter = "Perimeter: " + str(round(side_a + side_b + side_c, 2))

    # calculate area
    s = (side_a + side_b + side_c) / 2
    area = "Area: " + str(round(math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c)), 2))

    # draw triangle
    triangle = Polygon(point1, point2, point3)
    triangle.draw(win)

    instructions.setText("Click again to close")

    # area display
    area_point = Point(width / 2, height - 90)
    area = Text(area_point, area)
    area.draw(win)

    # perimeter display
    perimeter_point = Point(width / 2, height - 70)
    perimeter = Text(perimeter_point, perimeter)
    perimeter.draw(win)

    win.getMouse()
    win.close()

def color_shape():
    win = GraphWin("Color Circle", width, height)

    instruction_point = Point(width / 2, height - 350)
    instructions = Text(instruction_point, "Enter RGB values then click to color circle")
    instructions.draw(win)

    circle = Circle(Point(400, 200), 100)
    circle.draw(win)

    # RGB values
    red = 255
    green = 255
    blue = 255

    for i in range(5):
        red_instruction = Text(Point(275, 340), "Red: ")
        red_instruction.draw(win)
        red_entry = Entry(Point(400, 340), 30)
        red_entry.draw(win)

        green_instruction = Text(Point(275, 360), "Green: ")
        green_instruction.draw(win)
        green_entry = Entry(Point(400, 360), 30)
        green_entry.draw(win)

        blue_instruction = Text(Point(275, 380), "Blue: ")
        blue_instruction.draw(win)
        blue_entry = Entry(Point(400, 380), 30)
        blue_entry.draw(win)

        win.getMouse()

        red = eval(red_entry.getText())
        green = eval(green_entry.getText())
        blue = eval(blue_entry.getText())

        circle.setFill(color_rgb(red, green, blue))

    instructions.setText("Click again to close")

    win.getMouse()
    win.close()

def process_string():
    string = input("Enter text to process")

    first_character = string[0]
    last_character = string[- 1]
    middle_characters = string[1:5]
    concatenation = first_character + last_character
    first_three_characters = string[0:3]
    string_length = str(len(string))

    print("First character: ", first_character, "\n")
    print("Last character: ", last_character, "\n")
    print("Middle characters: ", middle_characters, "\n")
    print("First and last concatenation: ", concatenation, "\n")
    print("First three characters, repeated: ", end = "")

    for i in range(10):
        print(first_three_characters, end = "")
    print("\n")

    print("Each character, printed one per line: ")

    for i in range(len(string)):
        print(string[i])
    print("\n")

    print("String length: ", string_length)

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = ""
    for i in range(5):
        x += values[1]
    print(x)

    x = values[2:5]
    print(x)

    x = [str(values[2]), values[3], str(values[0])]
    print(x)

    x = [values[2], values[0], float(values[5])]
    print(x)

    x = values[2] + float(values[0]) + float(values[5])
    print(x)

    x = len(values)
    print(x)

def another_series():
    terms = eval(input("How many terms do you want to sum?"))
    pattern = [2, 4, 6]
    sum_accum = 0

    for i in range(terms):
        print(pattern[i % 3], end = " ")
        sum_accum += pattern[i % 3]
    print("")
    print("Sum:", sum_accum)

def target():
    win = GraphWin("Target", 362, 362)

    radius = 400 / 21

    instruction_point = Point(181, 10)
    instructions = Text(instruction_point, "Click to close")
    instructions.draw(win)

    white1 = Circle(Point(181,181), radius / 2 + radius * 9)
    white1.draw(win)

    white2 = Circle(Point(181,181), radius / 2 + radius * 8)
    white2.draw(win)

    black1 = Circle(Point(181,181), radius / 2 + radius * 7)
    black1.setFill("black")
    black1.draw(win)

    black2 = Circle(Point(181,181), radius / 2 + radius * 6)
    black2.setFill("black")
    black2.draw(win)

    blue1 = Circle(Point(181,181), radius / 2 + radius * 5)
    blue1.setFill("blue")
    blue1.draw(win)

    blue2 = Circle(Point(181,181), radius / 2 + radius * 4)
    blue2.setFill("blue")
    blue2.draw(win)

    red1 = Circle(Point(181,181), radius / 2 + radius * 3)
    red1.setFill("red")
    red1.draw(win)

    red2 = Circle(Point(181,181), radius / 2 + radius * 2)
    red2.setFill("red")
    red2.draw(win)

    yellow1 = Circle(Point(181,181), radius / 2 + radius)
    yellow1.setFill("yellow")
    yellow1.draw(win)

    yellow2 = Circle(Point(181,181), radius / 2)
    yellow2.setFill("yellow")
    yellow2.draw(win)

    win.getMouse()
    win.close()