import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_count_Odd_Squares(self):
        self.assertEqual(count_Odd_Squares(1, 25), 2)
        self.assertEqual(count_Odd_Squares(10, 25), 1)
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 100), 5)
        self.assertEqual(count_Odd_Squares(100, 200), 1)
        self.assertEqual(count_Odd_Squares(10000, 1000000), 10)
