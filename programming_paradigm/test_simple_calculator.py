# test_simple_calculator.py

import unittest
import simple_calculator

class TestSimpleCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(simple_calculator.add(1, 2), 3)
        self.assertEqual(simple_calculator.add(-1, 1), 0)
        self.assertEqual(simple_calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(simple_calculator.subtract(2, 1), 1)
        self.assertEqual(simple_calculator.subtract(-1, 1), -2)
        self.assertEqual(simple_calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(simple_calculator.multiply(2, 3), 6)
        self.assertEqual(simple_calculator.multiply(-1, 1), -1)
        self.assertEqual(simple_calculator.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(simple_calculator.divide(6, 3), 2)
        self.assertEqual(simple_calculator.divide(-1, 1), -1)
        self.assertEqual(simple_calculator.divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            simple_calculator.divide(1, 0)

if __name__ == '__main__':
    unittest.main()