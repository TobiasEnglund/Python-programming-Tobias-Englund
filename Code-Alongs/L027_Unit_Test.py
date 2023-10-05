from L026_Module import square, greet

def test_square_positive_numbers():
    assert square(2) == 4
    assert square(5) == 25
    
def test_square_negative_numbers(): 
    assert square(-2) == 4
    assert square(-5) == 25
    
def test_zero_square(): 
    assert square(0) == 0
    
def test_greet_default_no_name():
    assert greet() == "Hello world!"
    
def test_greet_with_name():
    assert greet("Fredrik") == "Hello Fredrik!" 