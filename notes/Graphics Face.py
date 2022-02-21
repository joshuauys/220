from graphics import Point, GraphWin, Circle

win = GraphWin("Face", 700, 700)
head = Circle(Point(350, 100), 100)
left_eye = Circle(Point(325, 60), 20)
right_eye = Circle(Point(475, 60), 20)

head.setFill("yellow")

left_eye.setOutline("red")
right_eye.setOutline("red")

left_eye.draw(win)
right_eye.draw(win)
head.draw(win)

input("hit enter to close")