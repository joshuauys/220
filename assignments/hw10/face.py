from graphics import Circle, Line, Polygon, Point


class Face:
    def __init__(self, window, center, size):
        self.eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.center = center
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, self.eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, self.eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        self.point_1 = center.clone()
        self.point_1.move(-mouth_size / 2, mouth_off)
        self.point_2 = center.clone()
        self.point_2.move(mouth_size / 2, mouth_off)
        self.point_3 = center.clone()
        self.point_3.move(mouth_size / 13, mouth_off + size / 4)
        self.mouth = Line(self.point_1, self.point_2)
        self.mouth.draw(window)

    def smile(self):
        self.mouth = Polygon(self.point_1, self.point_2, self.point_3)
        self.mouth.draw(self.window)

    def shock(self):
        self.mouth.undraw()
        self.mouth = Circle(self.center, self.eye_size)
        self.mouth.draw(self.window)

    def wink(self):
        self.left_eye.undraw()
        self.left_eye = Line(self.center)
        self.left_eye.draw(self.window)

