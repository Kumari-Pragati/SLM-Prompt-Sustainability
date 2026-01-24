import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(4, 9), 2)
        self.assertEqual(count_Odd_Squares(9, 16), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(count_Odd_Squares(0, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(4, 1), 0)
        self.assertEqual(count_Odd_Squares(16, 25), 4)
        self.assertEqual(count_Odd_Squares(25, 16), 0)

    def test_complex(self):
        self.assertEqual(count_Odd_Squares(20, 39), 4)
        self.assertEqual(count_Odd_Squares(39, 64), 5)
        self.assertEqual(count_Odd_Squares(64, 81), 5)
        self.assertEqual(count_Odd_Squares(81, 100), 5)
