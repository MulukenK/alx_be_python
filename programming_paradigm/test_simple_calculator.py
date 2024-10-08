import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):

        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2.5, 2), -0.5)
 
    def test_subtraction(self):

        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-1.5, -1), -0.5)
    
    def test_multiplication(self):

        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1.5, 3), -4.5)

    def test_division(self):
        
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(3, 0), None)
        self.assertEqual(self.calc.divide(3.3, 3), 1.1)