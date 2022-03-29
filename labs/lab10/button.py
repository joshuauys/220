"""
Name: Joshua Uys

lab10.py

Three Door Game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Rectangle, Point, Text, GraphWin

class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text

    def set_label(self, label):
        self.text.setText(label)

    def win(self, win):
        self.text.draw(win)
        self.shape.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, click):
        top_left_button = self.shape.getP1()
        bottom_right_button = self.shape.getP2()

        is_clicked = False

        if click.getX() < bottom_right_button.getX() and click.getX() > top_left_button.getX() and click.getY() > top_left_button.getY() and click.getY() < bottom_right_button.getY():
            is_clicked = True

        return is_clicked

    def color_button(self, color):
        self.shape.setFill(color)


