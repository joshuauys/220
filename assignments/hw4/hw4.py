"""
Name: Joshua Uys
hw4.py

Problem: General graphics program

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import graphics

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = graphics.GraphWin("Clicks", width, height)

    # number of times user can place a square
    num_clicks = 6

    # create a space to instruct user
    inst_pt = graphics.Point(width / 2, height - 10)
    instructions = graphics.Text(inst_pt, "Click to place a square")
    instructions.draw(win)

    # builds a square
    shape = graphics.Polygon()

    # allows the user to click multiple times to place a square
    for i in range(num_clicks):
        click = win.getMouse()
        click_x = click.getX()

        click_y = click.getY()

        top_left = graphics.Point(click_x - 25, click_y + 25)
        top_right = graphics.Point(click_x + 25, click_y + 25)
        bottom_left = graphics.Point(click_x - 25, click_y - 25)
        bottom_right = graphics.Point(click_x + 25, click_y - 25)

        shape = graphics.Polygon(top_left, top_right, bottom_right, bottom_left)
        shape.setFill("red")
        shape.setOutline("red")
        shape.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

def rectangle():
    win = graphics.GraphWin("Rectangle", 400, 400)

    inst_pt = graphics.Point(400 / 2, 400 - 70)
    instructions = graphics.Text(inst_pt, "Click to place the top left corner of your rectangle")
    instructions.draw(win)



    top_left = win.getMouse()
    instructions.setText("Click to place the bottom right corner of your rectangle")
    bottom_right = win.getMouse()
    instructions.setText("Click again to close")

    print("bottom right x=", bottom_right.getX())
    print("top left x=", top_left.getX())


    top_right = graphics.Point(bottom_right.getX(), top_left.getY())
    bottom_left = graphics.Point(top_left.getX(), bottom_right.getY())

    area = (bottom_right.getX() - bottom_left.getX()) * (bottom_left.getY() - top_left.getY())
    area_string = "Area: ", str(area)

    area_pt = graphics.Point(400 / 2, 400 - 50)
    area_text = graphics.Text(area_pt, area_string)
    area_text.draw(win)

    perimeter = (bottom_right.getX() - bottom_left.getX()) * 2 + \
                (bottom_left.getY() - top_left.getY()) * 2
    perimeter_string = "Perimeter: ", str(perimeter)

    perimeter_text = graphics.Text(graphics.Point(400 / 2, 400 - 30), perimeter_string)
    perimeter_text.draw(win)

    shape = graphics.Polygon(top_left, top_right, bottom_right, bottom_left)
    shape.setFill("green")
    shape.draw(win)

    win.getMouse()
    win.close()

def circle():
    width = 400
    height = 400
    win = graphics.GraphWin("Circle", width, height)

    inst_pt = graphics.Point(width / 2, height - 100)
    instructions = graphics.Text(inst_pt, "Click to mark the center of the circle")
    instructions.draw(win)

    center = win.getMouse()
    print("Center=", center)

    instructions.setText("Click a point on the circle's circumference")


    circumference_point = win.getMouse()
    print("Circumference=", circumference_point)

    radius = math.sqrt((center.getX()-circumference_point.getX())**2 +
                       (center.getY()-circumference_point.getY())**2)
    print("Radius=", radius)

    my_circle = graphics.Circle(center, radius)
    my_circle.draw(win)
    my_circle.setFill("light blue")

    radius_string = str(radius)
    radius_display_text = ("Radius", radius_string)

    radius_pt = graphics.Point(width / 2, height - 10)
    radius_display = graphics.Text(radius_pt, radius_display_text)
    radius_display.draw(win)

    instructions.setText("Click again to close")
    win.getMouse()
    win.close()

def pi2():
    terms = eval(input("Enter the number of terms to sum: "))
    denom_accum = 1
    previous_result = 0

    for i in range(terms):
        fraction = 4 / denom_accum
        # print("Fraction = 4 /", denom_accum)
        denom_accum += 2

        previous_result *= -1

        result = fraction + previous_result
        previous_result = result
        # print("result = ", result)

    result = abs(result)
    print("pi approximation: ", result)
    print("accuracy: ", abs(math.pi - result))

if __name__ == '__main__':
    pass
