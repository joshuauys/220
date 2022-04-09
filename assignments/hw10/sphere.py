from math import pi

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        surface_area = 4 * pi * (self.radius ** 2)
        return surface_area

    def volume(self):
        volume = (4 / 3) * pi * (self.radius ** 3)
        return volume
