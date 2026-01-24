import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):

    def test_simple_case(self):
        self.assertListEqual(perfect_squares(1, 16), [1, 4, 9, 16])

    def test_empty_range(self):
        self.assertListEqual(perfect_squares(0, 0), [])

    def test_single_number(self):
        self.assertListEqual(perfect_squares(4, 4), [4])

    def test_negative_numbers(self):
        self.assertListEqual(perfect_squares(-1, 0), [])
        self.assertListEqual(perfect_squares(0, -1), [])
        self.assertListEqual(perfect_squares(-1, -4), [4, 9])

    def test_large_numbers(self):
        self.assertListEqual(perfect_squares(100, 200), [49, 100, 121, 144, 169, 196])

    def test_no_perfect_squares(self):
        self.assertListEqual(perfect_squares(1, 4), [])
