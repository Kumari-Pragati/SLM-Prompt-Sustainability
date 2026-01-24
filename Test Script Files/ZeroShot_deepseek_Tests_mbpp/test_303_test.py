import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_solve_true(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))
        self.assertTrue(solve([1, 2, 3, 4, 5, 6], 6))
        self.assertTrue(solve([1, 2, 3, 4, 5, 6, 7], 7))

    def test_solve_false(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))
        self.assertFalse(solve([1, 2, 3, 4, 5, 4], 6))
        self.assertFalse(solve([1, 2, 3, 4, 5, 6, 5], 7))
