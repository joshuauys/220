"""
Name: Joshua Uys

lab11.py

Three Door Game II

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Text, Point, Rectangle
# from lab10.button import Button
from door import Door
from random import randint

continue_playing = True
win_counter = 0
loss_counter = 0

# Window
width = 800
height = 800
win = GraphWin("3 Door Game", width, height)

quit_button = Rectangle(Point(650, 50), Point(750, 100))
quit_button.draw(win)

quit_text = Text(Point(700, 75), "Quit")
quit_text.draw(win)

win_score_box = Rectangle(Point(50, 50), Point(100, 100))
win_score_box.draw(win)

lose_score_box = Rectangle(Point(100, 50), Point(150, 100))
lose_score_box.draw(win)

win_score_label = Text(Point(75, 45), "Wins")
win_score_label.draw(win)

lose_score_label = Text(Point(125, 45), "Losses")
lose_score_label.draw(win)

win_score = Text(Point(75, 75), "0")
win_score.draw(win)

lose_score = Text(Point(125, 75), "0")
lose_score.draw(win)

top_instructions = Text(Point(400, 200), "I have a secret door")
top_instructions.draw(win)

bottom_instructions = Text(Point(400, 725), "Click to guess which is the secret door")
bottom_instructions.draw(win)

while continue_playing:

    # Door variables
    door1_shape = Rectangle(Point(50, 300), Point(250, 650))
    door1_label = "closed"
    door1 = Door(door1_shape, door1_label)
    door1.close("burlywood4", "Closed")
    door1.draw(win)

    door2_shape = Rectangle(Point(300, 300), Point(500, 650))
    door2_label = "closed"
    door2 = Door(door2_shape, door2_label)
    door2.close("burlywood4", "Closed")
    door2.draw(win)

    door3_shape = Rectangle(Point(550, 300), Point(750, 650))
    door3_label = "closed"
    door3 = Door(door3_shape, door3_label)
    door3.close("burlywood4", "Closed")
    door3.draw(win)

    # generating random door
    random_door = randint(1,3)

    if random_door == 1:
        door1.set_secret(True)
        door2.set_secret(False)
        door3.set_secret(False)

    if random_door == 2:
        door1.set_secret(False)
        door2.set_secret(True)
        door3.set_secret(False)

    if random_door == 3:
        door1.set_secret(False)
        door2.set_secret(False)
        door3.set_secret(True)

    # clicks
    click = win.getMouse()
    clickx = click.getX()
    clicky = click.getY()

    # click quit?
    if clickx < 750 and clickx > 650 and clicky > 50 and clicky < 100:
        continue_playing = False
        win.close()

    # click door 1?
    if clickx < 250 and clickx > 50 and clicky > 300 and clicky < 650:
        if door1.is_secret() == True:
            door1.open("green", "open")
            win_counter += 1
            top_instructions.setText("You win")
        if door1.is_secret() == False:
            door1.open("red", "open")
            loss_counter += 1
            top_instructions.setText("You lose")

    # click door 2?
    if clickx < 500 and clickx > 300 and clicky > 300 and clicky < 650:
        if door2.is_secret() == True:
            door2.open("green", "open")
            win_counter += 1
            top_instructions.setText("You win")
        if door2.is_secret() == False:
            door2.open("red", "open")
            loss_counter += 1
            top_instructions.setText("You lose")

    # click door 3?
    if clickx < 750 and clickx > 550 and clicky > 300 and clicky < 650:
        if door3.is_secret() == True:
            door3.open("green", "open")
            win_counter += 1
            top_instructions.setText("You win")
        if door3.is_secret() == False:
            door3.open("red", "open")
            loss_counter += 1
            top_instructions.setText("You lose")

    win_score.setText(str(win_counter))
    lose_score.setText(str(loss_counter))
    bottom_instructions.setText("click anywhere to play again")
    click = win.getMouse()
    clickx = click.getX()
    clicky = click.getY()
    if clickx < 750 and clickx > 650 and clicky > 50 and clicky < 100:
        continue_playing = False
        win.close()
    top_instructions.setText("I have a secret door")
    bottom_instructions.setText("Click to guess which is the secret door")
    random_door = randint(1,3)