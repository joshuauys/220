#use .close

"""
Name: Joshua Uys
Valentines Card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time

from graphics import Point, Circle, Polygon, GraphWin, Text

def greeting_card():
    width = 800
    height = 400
    win = GraphWin("Happy Valentine's Day", width, height)
    win.setBackground("pink")

    def draw_heart():
        left_lobe = Circle(Point(150, 150), 50)
        right_lobe = Circle(Point(250, 150), 50)
        triangle = Polygon(Point(106.7, 175), Point(200, 300), Point(293.3, 175), Point(200, 150))

        left_lobe.setFill("red")
        right_lobe.setFill("red")
        triangle.setFill("red")

        left_lobe.setOutline("red")
        right_lobe.setOutline("red")
        triangle.setOutline("red")

        left_lobe.draw(win)
        right_lobe.draw(win)
        triangle.draw(win)

    draw_heart()

    def write_text():
        greeting = Text(Point(500, 150), "Happy")
        greeting.setStyle("bold")
        greeting.setSize(36)
        greeting.draw(win)

        greeting = Text(Point(550,200), "Valentines")
        greeting.setStyle("bold")
        greeting.setSize(36)
        greeting.draw(win)

        greeting = Text(Point(560,250), "Day")
        greeting.setStyle("bold")
        greeting.setSize(36)
        greeting.draw(win)

    write_text()

    stem = Polygon(Point(350, 300), Point(300, 250))
    head = Polygon(Point(285, 265), Point(315, 235), Point(280, 235))

    def draw_arrow():
        stem.setWidth(7)
        head.setWidth(7)
        head.setFill("black")
        stem.draw(win)
        head.draw(win)

    draw_arrow()

    center = Circle(Point(220, 190), 45)
    center.draw(win)
    center.setFill("red")
    center.setOutline("red")

    for i in range(3):
        for i in range(20):
            stem.move(-i, -i)
            head.move(-i,-i)
            time.sleep(0.07)
        stem.move(200, 200)
        head.move(200, 200)

    inst_pt = Point(width / 2, height - 50)
    instructions = Text(inst_pt, "Click to close")
    instructions.draw(win)

    win.getMouse()
    win.close()


greeting_card()