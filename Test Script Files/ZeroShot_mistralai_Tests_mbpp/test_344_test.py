import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_count_odd_squares(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(2, 9), 2)
        self.assertEqual(count_Odd_Squares(3, 16), 3)
        self.assertEqual(count_Odd_Squares(4, 25), 3)
        self.assertEqual(count_Odd_Squares(5, 36), 4)
        self.assertEqual(count_Odd_Squares(6, 49), 4)
        self.assertEqual(count_Odd_Squares(7, 64), 5)
        self.assertEqual(count_Odd_Squares(8, 81), 5)
        self.assertEqual(count_Odd_Squares(9, 100), 6)
