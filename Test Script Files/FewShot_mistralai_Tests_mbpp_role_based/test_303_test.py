import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(solve([1, 2, 3, 4], 4))
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_empty_list(self):
        self.assertFalse(solve([]))

    def test_negative_numbers(self):
        self.assertFalse(solve([-1, -2, -3], 3))

    def test_single_number(self):
        self.assertTrue(solve([1], 1))
        self.assertFalse(solve([-1], 1))

    def test_zero(self):
        self.assertTrue(solve([0], 1))

    def test_negative_numbers_and_zero(self):
        self.assertFalse(solve([-1, 0], 2))

    def test_large_numbers(self):
        self.assertTrue(solve([sys.maxsize, sys.maxsize * 2], sys.maxsize))

    def test_small_numbers(self):
        self.assertTrue(solve([-sys.maxsize, -sys.maxsize * 2], sys.maxsize))
