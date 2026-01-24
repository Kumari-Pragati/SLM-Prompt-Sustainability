import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_count_Odd_Squares(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(2, 4), 1)
        self.assertEqual(count_Odd_Squares(3, 9), 2)
        self.assertEqual(count_Odd_Squares(4, 16), 2)
        self.assertEqual(count_Odd_Squares(5, 25), 3)
        self.assertEqual(count_Odd_Squares(6, 36), 3)
        self.assertEqual(count_Odd_Squares(7, 49), 4)
        self.assertEqual(count_Odd_Squares(8, 64), 4)
        self.assertEqual(count_Odd_Squares(9, 81), 5)
        self.assertEqual(count_Odd_Squares(10, 100), 5)

    def test_count_Odd_Squares_edge_cases(self):
        self.assertEqual(count_Odd_Squares(0, 0), 0)
        self.assertEqual(count_Odd_Squares(0, 1), 0)
        self.assertEqual(count_Odd_Squares(0, 2), 0)
        self.assertEqual(count_Odd_Squares(0, 3), 0)
        self.assertEqual(count_Odd_Squares(0, 4), 0)
        self.assertEqual(count_Odd_Squares(0, 5), 0)
        self.assertEqual(count_Odd_Squares(0, 6), 0)
        self.assertEqual(count_Odd_Squares(0, 7), 0)
        self.assertEqual(count_Odd_Squares(0, 8), 0)
        self.assertEqual(count_Odd_Squares(0, 9), 0)
