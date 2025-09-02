import unittest
import sys
import os

# Add src to path to import the calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class"""

    def setUp(self):
        """Set up test fixtures before each test method"""
        self.calc = Calculator()

    def tearDown(self):
        """Clean up after each test method"""
        pass

    def test_add_integers(self):
        """Test addition of two integers"""
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        """Test addition of two floats"""
        result = self.calc.add(2.5, 3.7)
        self.assertAlmostEqual(result, 6.2)

    def test_add_negative_numbers(self):
        """Test addition of negative numbers"""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)

    def test_subtract_numbers(self):
        """Test subtraction"""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply_numbers(self):
        """Test multiplication"""
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)

    def test_divide_numbers(self):
        """Test division"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        """Test division by zero raises ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_power_positive(self):
        """Test power calculation with positive exponent"""
        result = self.calc.power(2, 3)
        self.assertEqual(result, 8)

    def test_power_zero(self):
        """Test power calculation with zero exponent"""
        result = self.calc.power(5, 0)
        self.assertEqual(result, 1)

    def test_add_invalid_input(self):
        """Test that add raises ValueError for non-numeric input"""
        with self.assertRaises(ValueError):
            self.calc.add("2", 3)

    def test_divide_invalid_input(self):
        """Test that divide raises ValueError for non-numeric input"""
        with self.assertRaises(ValueError):
            self.calc.divide("10", 2)

    def test_power_negative_exponent(self):
        """Test power with negative exponent"""
        result = self.calc.power(4, -1)
        self.assertAlmostEqual(result, 0.25)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for the Calculator class"""

    def setUp(self):
        self.calc = Calculator()

    def test_add_large_numbers(self):
        """Test addition of large numbers"""
        result = self.calc.add(1e6, 2e6)
        self.assertEqual(result, 3e6)

    def test_divide_small_numbers(self):
        """Test division of very small numbers"""
        result = self.calc.divide(1e-6, 2)
        self.assertEqual(result, 5e-7)


if __name__ == '__main__':
    # Run tests with detailed output
    unittest.main(verbosity=2)