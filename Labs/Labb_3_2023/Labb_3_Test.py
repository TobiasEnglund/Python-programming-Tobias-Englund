import Labb_3_Classes
import pytest
import 
from Labb_3_Classes import Rectangle, Circle

# Testing Rectangle

def test_rectangle_area():
    rect = Rectangle(4, 5)
    assert rect.area == 20

def test_rectangle_circumference():
    rect = Rectangle(4, 5)
    assert rect.circumference == 18  # because: 2*(4+5)

def test_is_square():
    square = Rectangle(5, 5)
    non_square = Rectangle(4, 5)
    assert square.is_square() == True
    assert non_square.is_square() == False

# Testing Circle

def test_circle_area():
    circle = Circle(3)
    assert circle.area == 3 * 3 * pi    # pytest.approx(28.27, 0.01)  # 3*3*pi

def test_circle_circumference():
    circle = Circle(3)
    assert circle.circumference == pytest.approx(18.85, 0.01)  # 2*3*pi

def test_is_unit_circle():
    unit_circle = Circle(1)
    non_unit_circle = Circle(3)
    assert unit_circle.is_unit_circle() == True
    assert non_unit_circle.is_unit_circle() == False

# def test_square_positive_numbers():
#     assert square(2) == 4
#     assert square(5) == 25
    
# def test_square_negative_numbers(): 
#     assert square(-2) == 4
#     assert square(-5) == 25
    
# def test_zero_square(): 
#     assert square(0) == 0
    
# def test_greet_default_no_name():
#     assert greet() == "Hello world!"
    
# def test_greet_with_name():
#     assert greet("Fredrik") == "Hello Fredrik!" 