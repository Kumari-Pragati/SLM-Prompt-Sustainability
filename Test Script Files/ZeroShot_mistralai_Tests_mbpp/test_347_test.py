import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_count_squares_with_equal_dimensions(self):
        self.assertEqual(count_Squares(3, 3), 28)
        self.assertEqual(count_Squares(4, 4), 84)
        self.assertEqual(count_Squares(5, 5), 165)

    def test_count_squares_with_different_dimensions(self):
        self.assertEqual(count_Squares(3, 4), 40)
        self.assertEqual(count_Squares(4, 5), 70)
        self.assertEqual(count_Squares(5, 6), 132)

    def test_count_squares_with_zero_or_negative_dimensions(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(-1, 2), 0)
        self.assertEqual(count_Squares(2, -3), 0)
