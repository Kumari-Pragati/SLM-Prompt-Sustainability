import unittest
from mbpp_303_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_true(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_solve_false(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_solve_true_empty(self):
        self.assertTrue(solve([], 0))

    def test_solve_false_empty(self):
        self.assertFalse(solve([5], 1))

    def test_solve_true_single(self):
        self.assertTrue(solve([1], 1))

    def test_solve_false_single(self):
        self.assertFalse(solve([5], 1))

    def test_solve_true_negative(self):
        self.assertTrue(solve([-1, -2, -3, -4, -5], 5))

    def test_solve_false_negative(self):
        self.assertFalse(solve([-5, -4, -3, -2, -1], 5))
