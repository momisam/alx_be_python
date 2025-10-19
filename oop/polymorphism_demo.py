import math

# Base Class
class Shape:
    def area(self):
        # This enforces that subclasses must implement their own area method
        raise NotImplementedError("Subclasses must override this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
