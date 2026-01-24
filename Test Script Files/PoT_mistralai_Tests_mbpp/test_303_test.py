import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertTrue(solve([10, 20, 30, 40, 50], 5))

    def test_edge_case_min_length(self):
        self.assertTrue(solve([1], 1))
        self.assertFalse(solve([], 1))

    def test_edge_case_max_length(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 6))
        self.assertFalse(solve([1, 2, 3, 4, 5], 0))

    def test_edge_case_zero(self):
        self.assertTrue(solve([0], 1))

    def test_edge_case_negative(self):
        self.assertFalse(solve([-1, -2, -3], 3))

    def test_corner_case_decreasing(self):
        self.assertTrue(solve([5, 4, 3, 2, 1], 5))

    def test_corner_case_increasing(self):
        self.assertFalse(solve([1, 2, 3, 4, 5], 1))
