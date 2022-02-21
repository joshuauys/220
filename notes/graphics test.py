import graphics

win = graphics.GraphWin("CSCI 220", 700, 700)


click = win.getMouse()
print(click)

click2 = win.getMouse()
print(click2)

click3 = win.getMouse()
print(click3)

shape = graphics.Polygon(click, click2, click3)

shape.draw(win)

win.getMouse()