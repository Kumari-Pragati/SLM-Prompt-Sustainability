import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_empty_range(self):
        self.assertListEqual(perfect_squares(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(perfect_squares(1, 1), [])
        self.assertListEqual(perfect_squares(4, 4), [4])
        self.assertListEqual(perfect_squares(9, 9), [3, 9])

    def test_multiple_numbers(self):
        self.assertListEqual(perfect_squares(1, 10), [])
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9, 16])
        self.assertListEqual(perfect_squares(20, 30), [4, 9, 16, 25])
        self.assertListEqual(perfect_squares(100, 121), [4, 9, 16, 25, 36, 49, 64, 81, 100])
