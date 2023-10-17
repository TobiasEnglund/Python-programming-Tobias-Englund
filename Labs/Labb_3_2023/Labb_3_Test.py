import unittest
from math import pi
from Labb_3_Classes import Shape, Rectangle, Circle, Cube, Sphere

# Received help from ChatGPT with finding ".assertEqual", ".assertTrue" and "unittest.TestCase"

class TestShapes(unittest.TestCase):
    
    # Test rectangle
    def test_rectangle_area(self):
        rectangle = Rectangle(0, 0, 4, 5)
        self.assertEqual(rectangle.area, 20)

    def test_rectangle_circumference(self):
        rectangle = Rectangle(0, 0, 4, 5)
        self.assertEqual(rectangle.circumference, 18)

    def test_rectangle_is_square(self):
        rectangle = Rectangle(0, 0, 4, 4)
        self.assertTrue(rectangle.is_square())
        
    # Test circle
    def test_circle_area(self):
        circle = Circle(0, 0, 2)
        self.assertEqual(circle.area, 4 * pi)
        
    def test_circle_circumference(self):
        circle = Circle(0, 0, 2)
        self.assertEqual(circle.circumference, 4 * pi)
        
    def test_circle_is_unit_circle(self):
        circle = Circle(0, 0, 1)
        self.assertTrue(circle.is_unit_circle())
      
    # Test cube  
    def test_cube_area(self):
        cube = Cube(0, 0, 0, 2)
        self.assertEqual(cube.area, 24)
        
    def test_cube_volume(self):
        cube = Cube(0, 0, 0, 2)
        self.assertEqual(cube.volume, 8)

    def test_cube_is_unit_cube(self):
        cube = Cube(0, 0, 0, 1)
        self.assertTrue(cube.is_unit_cube())
    
    # Test sphere
    def test_sphere_surface_area(self):
        sphere = Sphere(0, 0, 0, 2)
        self.assertEqual(sphere.area, 4 * 4 * pi)

    def test_sphere_volume(self):
        sphere = Sphere(0, 0, 0, 2)
        self.assertEqual(sphere.volume, (4/3) * pi * (2)**3)
        
    def test_sphere_is_unit_sphere(self):
        sphere = Sphere(0, 0, 0, 1)
        self.assertTrue(sphere.is_unit_sphere())