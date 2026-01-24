import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Odd_Squares(4, 25), 3)
        self.assertEqual(count_Odd_Squares(9, 36), 3)
        self.assertEqual(count_Odd_Squares(16, 25), 0)

    def test_zero(self):
        self.assertEqual(count_Odd_Squares(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Odd_Squares(-1, 4), 0)
        self.assertEqual(count_Odd_Squares(-4, 9), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, count_Odd_Squares, -1, 0)
        self.assertRaises(ValueError, count_Odd_Squares, 0, -1)
        self.assertRaises(ValueError, count_Odd_Squares, 0, 0)
