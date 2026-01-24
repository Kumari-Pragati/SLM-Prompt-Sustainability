import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_empty_range(self):
        self.assertListEqual(perfect_squares(0, 0), [])

    def test_single_perfect_square(self):
        self.assertListEqual(perfect_squares(1, 1), [1])

    def test_multiple_perfect_squares(self):
        self.assertListEqual(perfect_squares(1, 9), [1, 4, 9])

    def test_end_of_range_not_perfect_square(self):
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9])

    def test_start_of_range_not_perfect_square(self):
        self.assertListEqual(perfect_squares(2, 9), [4, 9])

    def test_no_perfect_squares(self):
        self.assertListEqual(perfect_squares(10, 121), [])

    def test_large_range(self):
        self.assertListEqual(perfect_squares(1, 1000000), list(range(1, 101)) + list(range(103, 1001, 4)))
