import unittest
from mbpp_303_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertTrue(solve([10, 20, 30, 40, 50], 5))

    def test_edge_cases(self):
        self.assertTrue(solve([0, 1, 2, 3, 4], 5))
        self.assertTrue(solve([1, 0, 2, 3, 4], 5))
        self.assertTrue(solve([1, 2, 0, 3, 4], 5))
        self.assertTrue(solve([1, 2, 3, 0, 4], 5))
        self.assertTrue(solve([1, 2, 3, 4, 0], 5))

    def test_boundary_cases(self):
        self.assertTrue(solve([1], 1))
        self.assertTrue(solve([1, 2], 2))
        self.assertTrue(solve([1, 2, 3], 3))
        self.assertTrue(solve([1, 2, 3, 4], 4))
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_negative_numbers(self):
        self.assertTrue(solve([-1, -2, -3, -4, -5], 5))

    def test_zero_input(self):
        self.assertFalse(solve([], 0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, solve, "a", 1)
        self.assertRaises(TypeError, solve, [1], "n")
        self.assertRaises(ValueError, solve, [], -1)
        self.assertRaises(ValueError, solve, [1], -1)
