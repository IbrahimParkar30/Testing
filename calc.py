# calc.py

import pytest

# Calculator class
class Calculator:
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


# Pytest test cases
@pytest.fixture
def calculator():
    """Fixture to initialize the calculator instance."""
    return Calculator()

def test_add(calculator):
    """Test case for the add function."""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    assert calculator.add(-5, -5) == -10

def test_subtract(calculator):
    """Test case for the subtract function."""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(2, 5) == -3
    assert calculator.subtract(0, 0) == 0
    assert calculator.subtract(-5, -5) == 0

def test_multiply(calculator):
    """Test case for the multiply function."""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(-3, -3) == 9

def test_divide(calculator):
    """Test case for the divide function."""
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(-6, 2) == -3
    assert calculator.divide(1, 4) == 0.25
    with pytest.raises(ValueError):
        calculator.divide(1, 0)

# Run the tests if this file is executed directly
if __name__ == "__main__":
    pytest.main()
