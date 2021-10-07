import pytest
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'

def subtract(a, b):
    return a + b  # <--- fix this 

# uncomment the following test
def test_subtract():
    assert subtract(2, 3) == -1

def test_add_float():
    epsilon = 1e-10
    assert abs(add(0.1, 0.2) - 0.3) < epsilon
    assert add(0.1, 0.2) == pytest.approx(0.3)
