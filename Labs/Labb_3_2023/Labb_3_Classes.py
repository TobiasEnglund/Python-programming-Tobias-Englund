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

# I didn't understand the math for the inside_object methods and ended up using ChatGPT for these.
# Tried using docstrings to comment the methods etc but I'm not sure if I did it correctly. Just 

class Shape():
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if not isinstance(other, Shape): 
            raise TypeError(f"Can't compare Shape with {type(other)}")
        return self.area == other.area
    
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can't compare Shape with {type(other)}")
        return self.area < other.area

    def __gt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can't compare Shape with {type(other)}")
        return self.area > other.area
    
    def __le__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can't compare Shape with {type(other)}")
        return self.area <= other.area
    
    def __ge__(self, other):
        if not isinstance(other, Shape):
            raise TypeError(f"Can't compare Shape with {type(other)}")
        return self.area >= other.area

    def translation(self, x, y, z):
        self.x += x
        self.y += y
        if hasattr(self, 'z'):
            self.z += z

    def inside_object(self, x, y, z):  # Code for inside_object method from ChatGPT 
        raise NotImplementedError("This method should be overridden by subclass")

    def __repr__(self):
        if self.z is not None:
            return f'The center point of the shape is located at x: {self.x}, y: {self.y}, and z: {self.z}.)'
        else:
            return f'The center point of the shape is located at x: {self.x} and y: {self.y}.)'
        
    def __str__(self):
        return "This is a shape object."

class Rectangle(Shape):
    """
    The Rectangle class is used for:
    - Calculating the area of the rectangle
    - Calculating the perimeter of the rectangle
    - Checking if the rectangle is a square
    - Checking if the center point is inside the rectangle
    """
    def __init__(self, x, y, width, length):
        super().__init__(x, y)
        if width < 0 or length < 0 or not isinstance(width, (int, float)) or not isinstance(length, (int, float)):
            raise ValueError("Sides of a rectangle must be positive.")
        self.width = width
        self.length = length
    
    @property
    def area(self): 
        return self.width * self.length

    @property
    def perimeter(self):    
        return (2 * self.width) + (2 * self.length)
    
    def is_square(self):
        """
        Checks if rectangle is a square
        
        Returns:
        True: If the rectangle is a square
        False: If it is not
        """
        return self.width == self.length
    
    def inside_object(self, x, y):  # Code (not docstrings) for inside_object method from ChatGPT 
        """
        Checks if the center point is inside the rectangle
        
        Returns:
        True: If the center point is inside the rectangle
        False: If it is not
        """
        return abs(x - self.x) <= self.width / 2 and abs(y - self.y) <= self.length / 2     
    
    def __repr__(self):
        return super().__repr__() + f'The rectangle has the sides {self.width} and {self.length}.'
    
    def __str__(self):
        return super().__str__() + f'The rectangle has the area {self.area} and perimeter {self.perimeter}.'
    
class Circle(Shape):
    """
    The Circle class is used for:
    - Calculating the area of the circle
    - Calculating the circumference of the circle
    - Checking if the circle is a unit circle
    - Checking if the center point is inside the circle
    """
    def __init__(self, x, y, radius): 
        super().__init__(x, y)
        if radius < 0 or not isinstance(radius, (int, float)):
            raise ValueError("The radius of a circle must be positive.")
        self.radius = radius
        
    @property
    def area(self):
        return pi * (self.radius)**2

    @property
    def circumference(self):
        return 2 * pi * self.radius  
    
    def is_unit_circle(self):
        """
        Checks if the circle is a unit circle

        Returns:
        True: If the cube is a unit circle
        False: If it is not
        """
        return self.radius == 1
            
    def inside_object(self, x, y):  # Code (not docstrings) for inside_object method from ChatGPT
        """
        Checks if the center point is inside the circle
        
        Returns:
        True: If the center point is inside the circle
        False: If it is not
        """
        return (x - self.x)**2 + (y - self.y)**2 <= self.radius**2                              
            
    def __repr__(self):
        return super().__repr__() + f'The circle has a radius of {self.radius}.'
    
    def __str__(self):
        return super().__str__() + f'The circle has the area {self.area} and circumference {self.circumference}.'

# For cubes and spheres (the 3D shapes) I decided to go with area and volume. To me, circumference don't really seem useful for 3D shapes.

# Cube formulas:
# Area = 6 * (side_length)^2
# Volume = (side_length)^3

class Cube(Shape):
    """
    The Cube class is used for:
    - Calculating the area of the cube
    - Calculating the volume of the cube
    - Checking if the cube is a unit cube
    - Checking if the center point is inside the cube
    """
    def __init__(self, x, y, z, side_length): 
        super().__init__(x, y, z)
        if side_length < 0 or not isinstance(side_length, (int, float)):
            raise ValueError("The side-length of a cube must be positive.")
        self.side_length = side_length
        
    @property
    def area(self):
        return 6 * (self.side_length)**2
    
    @property
    def volume(self):
        return (self.side_length)**3   
    
    def is_unit_cube(self):
        """
        Checks if the cube is a unit cube

        Returns:
        True: If the cube is a unit cube
        False: If it is not
        """
        return self.side_length == 1
            
    def inside_object(self, x, y, z):   # Code (not docstrings) for inside_object method from ChatGPT
        """
        Checks if the center point is inside the cube
        
        Returns:
        True: If the center point is inside the cube
        False: If it is not
        """
        return abs(x - self.x) <= self.side_length / 2 and \
            abs(y - self.y) <= self.side_length / 2 and \
            abs(z - self.z) <= self.side_length / 2        
            
    def __repr__(self):
        return super().__repr__() + f'The cube has a side-length of {self.side_length}.'
    
    def __str__(self):
        return super().__str__() + f'The cube has an area of {self.area} and a volume of {self.volume}..'

# Sphere formulas:
# Area = 4 * pi * (radius)^2
# Volume = pi * 4/3 * (radius)^3

class Sphere(Shape):
    """
    The Sphere class is used for:
    - Calculating the area of the sphere
    - Calculating the volume of the sphere
    - Checking if the sphere is a unit sphere
    - Checking if the center point is inside the sphere
    """
    
    def __init__(self, x, y, z, radius): 
        super().__init__(x, y, z)
        if radius < 0 or not isinstance(radius, (int, float)):
            raise ValueError("The radius of a sphere must be positive.")
        self.radius = radius
        
    @property
    def area(self):
        return pi * 4 * (self.radius)**2
    
    @property
    def volume(self):
        return pi * (4/3) * (self.radius)**3 
    
    def is_unit_sphere(self):
        """
        Checks if the sphere is a unit sphere

        Returns:
        True: If the sphere is the unit sphere
        False: If it is not
        """
        return self.radius == 1
            
    def inside_object(self, x, y, z):  # Code (not docstrings) for inside_object method from ChatGPT
        """
        Checks if the center point is inside the sphere
        
        Returns:
        bool True: If the center point is inside the sphere
        bool False: If it is not
        """
        return (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2 <= self.radius**2        
            
    def __repr__(self):
        return super().__repr__() + f'The sphere has a radius of {self.radius}.'
    
    def __str__(self):
        return super().__str__() + f'The sphere has a  area of {self.area} and a volume of {self.volume}.'