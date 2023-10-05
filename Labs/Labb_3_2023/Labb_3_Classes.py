# The classes should have:
# - An `area` property.
# - A `circumference` property.
# - An operator overload of `==` for equality check.
# - An operator overload of comparison operators `<`,`>`,`<=`,`>=` for comparisons.
# - An override of `__repr__()`.
# - An override of `__str__()`.
# - `x` and `y` which represent the center position of the object.
# - A translation method that allows movement of `x` and `y`.
# - A method that checks if a certain point is inside the object.
# - Error handling.
# - A method that checks if the circle instance is a unit circle.
# - A method that checks if the rectangle instance is a square.

from math import pi

class Figures():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def translation():
    #     pass

    def __repr__(self):
        return f'The center point of the figure is located at ({self.x, self.y})'
    
    def __str__(self):
        return

class Rectangle(Figures):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
    
    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def circumference(self):
        return (2 * self.side1) + (2 * self.side2)
    
    def is_square(self):
        if self.side1 == self.side2:
            print("It's a square!")
    
    def __repr__(self):
        return f'The rectangle has the sides {self.side1} and {self.side2}'
    
    def __str__(self):
        return
    
class Circle(Figures):
    def __init__(self, radius): 
        self.radius = radius
        
    @property
    def area(self):
        return pi * self.radius * self.radius

    @property
    def circumference(self):
        return 2 * pi * self.radius     
    
    def is_unit_circle(self):
        if self.radius == 1:
            print("It's the unit circle!")
            
    def __repr__(self):
        return f'The circle has a radius of {self.radius}'
    
    def __str__(self):
        return