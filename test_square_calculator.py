# test_square_calculator.py
import unittest
from square_calculator import square

class TestSquareCalculator(unittest.TestCase):

    def test_square_positive_number(self):
        self.assertEqual(square(4), 16)

    def test_square_negative_number(self):
        self.assertEqual(square(-3), 9)

    def test_square_float_number(self):
        self.assertEqual(square(2.5), 6.25)

if __name__ == '__main__':
    unittest.main()
