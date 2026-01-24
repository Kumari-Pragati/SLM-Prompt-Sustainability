import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertTrue(solve([5, 4, 3, 2, 1], 5))
        self.assertTrue(solve([1, 3, 2, 5, 4], 5))

    def test_edge_conditions(self):
        self.assertTrue(solve([], 0))
        self.assertTrue(solve([1], 1))
        self.assertFalse(solve([2, 1], 2))

    def test_boundary_conditions(self):
        self.assertTrue(solve([sys.maxsize], 1))
        self.assertFalse(solve([sys.maxsize, 2], 2))
        self.assertFalse(solve([-sys.maxsize - 1, -2], 2))

    def test_complex_cases(self):
        self.assertFalse(solve([5, 4, 3, 2, 1, 0], 6))
        self.assertFalse(solve([1, 2, 3, 4, 5, sys.maxsize], 6))
        self.assertFalse(solve([-sys.maxsize - 1, -2, -3, -4, -5], 5))
