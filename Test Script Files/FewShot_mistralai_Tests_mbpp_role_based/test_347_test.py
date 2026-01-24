import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(count_Squares(2, 3), 6)
        self.assertEqual(count_Squares(3, 3), 6)
        self.assertEqual(count_Squares(4, 4), 10)

    def test_zero(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_Squares(-1, 2), 0)
        self.assertEqual(count_Squares(2, -1), 0)
        self.assertEqual(count_Squares(-2, -3), 0)

    def test_one_argument(self):
        self.assertRaises(ValueError, count_Squares, 2)
        self.assertRaises(ValueError, count_Squares, -2)
