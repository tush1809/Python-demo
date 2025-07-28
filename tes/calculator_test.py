import pytest
import sys
import os


# Add src directory to path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator.calculator import Calculator


class TestCalculator:

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(5.0, 3.0)
        assert result == 8.0

    def test_subtract(self):
        result = self.calculator.subtract(10.0, 4.0)
        assert result == 6.0

    def test_multiply(self):
        result = self.calculator.multiply(3.0, 4.0)
        assert result == 12.0

    def test_divide(self):
        result = self.calculator.divide(15.0, 3.0)
        assert result == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(10.0, 0.0)