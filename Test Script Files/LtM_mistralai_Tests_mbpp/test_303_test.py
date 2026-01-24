import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(solve([1, 2, 3], 3))
        self.assertTrue(solve([4, 5, 6], 3))
        self.assertTrue(solve([7, 8, 9], 3))

    def test_edge_cases(self):
        self.assertTrue(solve([1], 1))
        self.assertTrue(solve([1, 2], 2))
        self.assertFalse(solve([1, 2, 3], 1))
        self.assertFalse(solve([1, 2, 3], 4))

    def test_boundary_conditions(self):
        self.assertFalse(solve([sys.maxsize], 1))
        self.assertFalse(solve([-sys.maxsize], 1))
        self.assertFalse(solve([-sys.maxsize, -sys.maxsize], 2))
        self.assertFalse(solve([sys.maxsize, sys.maxsize], 2))

    def test_complex_cases(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertFalse(solve([1, 2, 3, 4, 5, 6], 5))
        self.assertTrue(solve([-1, -2, -3, -4, -5], 5))
        self.assertFalse(solve([-1, -2, -3, -4, -5, -6], 5))
