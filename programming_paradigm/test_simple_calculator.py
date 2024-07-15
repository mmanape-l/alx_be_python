# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        calc = SimpleCalculator()  # Create an instance of SimpleCalculator
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        calc = SimpleCalculator()  # Create an instance of SimpleCalculator
        self.assertEqual(calc.subtract(2, 1), 1)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        calc = SimpleCalculator()  # Create an instance of SimpleCalculator
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        calc = SimpleCalculator()  # Create an instance of SimpleCalculator
        self.assertEqual(calc.divide(6, 3), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()