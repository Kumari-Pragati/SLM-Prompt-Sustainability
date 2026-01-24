import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(count_Squares(3, 5), 14)
        self.assertEqual(count_Squares(5, 7), 28)
        self.assertEqual(count_Squares(7, 9), 42)

    def test_same_integers(self):
        self.assertEqual(count_Squares(4, 4), 10)

    def test_negative_or_zero(self):
        self.assertRaises(ValueError, count_Squares, 0, 5)
        self.assertRaises(ValueError, count_Squares, -3, 5)

    def test_one_argument(self):
        self.assertRaises(TypeError, count_Squares, 5)

    def test_non_integer_arguments(self):
        self.assertRaises(TypeError, count_Squares, 5.0, 5)
        self.assertRaises(TypeError, count_Squares, 5, 5.0)

    def test_large_numbers(self):
        self.assertEqual(count_Squares(1000000, 1000001), 4999995000000)
