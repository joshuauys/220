"""
Name: Joshua Uys

lab11.py

Three Door Game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import Rectangle, Point, Text, GraphWin
from random import randint

class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.text.undraw()
        self.shape.undraw()

    def is_clicked(self, click):
        top_left_button = self.shape.getP1()
        bottom_right_button = self.shape.getP2()

        is_clicked_door = False

        if click.getX() < bottom_right_button.getX() and click.getX() > top_left_button.getX() and click.getY() > top_left_button.getY() and click.getY() < bottom_right_button.getY():
            is_clicked_door = True

        return is_clicked_door

    def open(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def close(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        return self.secret

    def set_secret(self, secret):
        self.secret = secret





