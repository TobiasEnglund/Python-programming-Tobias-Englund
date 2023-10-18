import unittest
from math import pi
from Labb_3_Classes import Shape, Rectangle, Circle, Cube, Sphere

# Received help from ChatGPT with finding "unittest.TestCase"

class TestShapes(unittest.TestCase):

    # Common Tests
    def test_translation(self):
        rectangle = Rectangle(0, 0, 4, 5)
        rectangle.translation(1, 2, None)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
    
    def test_equality(self):
        rectangle1 = Rectangle(0, 0, 4, 5)
        rectangle2 = Rectangle(0, 0, 4, 5)
        self.assertEqual(rectangle1, rectangle2)

    # Test rectangle
    def test_rectangle_area(self):
        rectangle = Rectangle(0, 0, 4, 5)
        self.assertEqual(rectangle.area, 20)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(0, 0, 4, 5)
        self.assertEqual(rectangle.perimeter, 18)

    def test_rectangle_is_square(self):
        rectangle = Rectangle(0, 0, 4, 4)
        self.assertTrue(rectangle.is_square())
        
    def test_rectangle_inside(self):
        rectangle = Rectangle(0, 0, 4, 5)
        self.assertTrue(rectangle.inside_object(1, 1))
        self.assertFalse(rectangle.inside_object(3, 3))

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
    
    def test_circle_inside(self):
        circle = Circle(0, 0, 2)
        self.assertTrue(circle.inside_object(1, 1))
        self.assertFalse(circle.inside_object(3, 3))

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

    def test_cube_inside(self):
        cube = Cube(0, 0, 0, 2)
        self.assertTrue(cube.inside_object(1, 1, 1))
        self.assertFalse(cube.inside_object(3, 3, 3))
    
    # Test sphere
    def test_sphere_surface_area(self):
        sphere = Sphere(0, 0, 0, 2)
        self.assertEqual(sphere.area, 4 * pi * 4)

    def test_sphere_volume(self):
        sphere = Sphere(0, 0, 0, 2)
        self.assertEqual(sphere.volume, (4/3) * pi * 8)
        
    def test_sphere_is_unit_sphere(self):
        sphere = Sphere(0, 0, 0, 1)
        self.assertTrue(sphere.is_unit_sphere())

    def test_sphere_inside(self):
        sphere = Sphere(0, 0, 0, 2)
        self.assertTrue(sphere.inside_object(1, 1, 1))
        self.assertFalse(sphere.inside_object(3, 3, 3))