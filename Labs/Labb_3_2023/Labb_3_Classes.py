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

class Shape():
    def __init__(self):
        pass

    def __eq__(self):
        pass
    
    def __lt__(self):
        pass

    def __gt__(self):
        pass
    
    def __le__(self):
        pass
    
    def __ge__(self):
        pass

    def translation(self):
        pass

    def inside_object(self):
        pass

    def __repr__(self):
        pass
        
    def __str__(self):
        pass
    
class Rectangle(Shape):
    def __init__(self):
        pass
    
    @property
    def area(self): 
        pass

    @property
    def perimeter(self):    
        pass
    
    def is_square(self):
        pass
    
    def inside_object(self):
        pass  
    
    def __repr__(self):
        pass
    
    def __str__(self):
        pass
    
class Circle(Shape):
    def __init__(self): 
        pass
        
    @property
    def area(self):
        pass

    @property
    def circumference(self):
        pass
    
    def is_unit_circle(self):
        pass
            
    def inside_object(self):
        pass                        
            
    def __repr__(self):
        pass
    
    def __str__(self):
        pass

class Cube(Shape):
    def __init__(self): 
        pass
        
    @property
    def area(self):
        pass
    
    @property
    def volume(self):
        pass
    
    def is_unit_cube(self):
        pass
            
    def inside_object(self): 
        pass     
            
    def __repr__(self):
        pass
    
    def __str__(self):
        pass

class Sphere(Shape):  
    def __init__(self): 
        pass
        
    @property
    def area(self):
        pass
    
    @property
    def volume(self):
        pass
    
    def is_unit_sphere(self):
        pass
            
    def inside_object(self):
        pass    
            
    def __repr__(self):
        pass
    
    def __str__(self):
        pass