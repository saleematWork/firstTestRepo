import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from calculator import Calculator

class TestCalculatorIntegration(unittest.TestCase):
    """Integration tests for the Calculator class"""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_complex_calculation_sequence(self):
        """Test a sequence of operations"""
        # (2 + 3) * 4 / 2
        step1 = self.calc.add(2, 3)
        step2 = self.calc.multiply(step1, 4)
        result = self.calc.divide(step2, 2)
        
        self.assertEqual(result, 10)
    
    def test_power_of_sum(self):
        """Test (a + b)^c"""
        sum_result = self.calc.add(2, 3)
        power_result = self.calc.power(sum_result, 2)
        
        self.assertEqual(power_result, 25)

if __name__ == '__main__':
    unittest.main(verbosity=2)