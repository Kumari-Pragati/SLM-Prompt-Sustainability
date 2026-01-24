import unittest
from mbpp_303_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_positive(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertTrue(solve([10, 20, 30, 40, 50], 5))
        self.assertTrue(solve([1, 2, 3, 4, 5, 6], 6))

    def test_solve_negative(self):
        self.assertFalse(solve([1, 2, 3, 4, 5], 6))
        self.assertFalse(solve([10, 20, 30, 40, 50], 4))
        self.assertFalse(solve([1, 2, 3, 4], 5))

    def test_edge_cases(self):
        self.assertTrue(solve([], 0))
        self.assertTrue(solve([0], 0))
        self.assertTrue(solve([0], 1))
        self.assertFalse(solve([0], 2))
