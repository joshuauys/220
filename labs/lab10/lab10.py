"""
Name: Joshua Uys

lab10.py

Three Door Game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Point, Rectangle
from button import Button
from door import Door

# Window
width = 400
height = 800
win = GraphWin("3 Door Game", width, height)

#Class Variables
exit_shape = Rectangle(Point(50, 50), Point(350, 250))
exit_label = "Exit"

door_shape = Rectangle(Point(50, 300), Point(350, 750))
door_label = "closed"

button = Button(exit_shape, exit_label)
door = Door(door_shape, door_label)

# Draw Buttons
button.win(win)
door.draw(win)

click = Point(0, 0)
door_tracker = 0

while button.is_clicked(click) == False:
    click = win.getMouse()

    if door.is_clicked(click):
        if door_tracker % 2 == 1:
            door.open("white", "open")
            door.undraw()
            door.draw(win)
        if door_tracker % 2 == 0:
            door.close("red", "closed")
            door.undraw()
            door.draw(win)
        door_tracker += 1

win.close()