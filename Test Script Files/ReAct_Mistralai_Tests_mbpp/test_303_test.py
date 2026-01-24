import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_solve_positive(self):
        # Typical case: increasing sequence
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_solve_negative_decreasing(self):
        # Typical case: decreasing sequence
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_solve_negative_duplicates(self):
        # Edge case: duplicate elements
        self.assertFalse(solve([1, 1, 2, 3, 4], 5))

    def test_solve_negative_out_of_range(self):
        # Edge case: out of range index
        self.assertRaises(IndexError, solve, [1, 2, 3], 4)

    def test_solve_negative_empty_list(self):
        # Edge case: empty list
        self.assertFalse(solve([], 0))

    def test_solve_negative_negative_numbers(self):
        # Edge case: negative numbers
        self.assertFalse(solve([-1, -2, -3], 3))
