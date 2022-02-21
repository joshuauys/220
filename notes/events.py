import graphics

win = graphics.GraphWin("Events", 700, 700)

click_point = win.getMouse()
print(click_point.getX())