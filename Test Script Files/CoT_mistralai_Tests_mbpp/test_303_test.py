import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_min_length(self):
        self.assertTrue(solve([1], 1))

    def test_edge_case_max_length(self):
        self.assertTrue(solve([1, 2, 3, 4, 5, 6], 6))

    def test_edge_case_empty_list(self):
        self.assertFalse(solve([], 1))

    def test_edge_case_negative_numbers(self):
        self.assertFalse(solve([-1, -2, 3], 3))

    def test_edge_case_zero(self):
        self.assertTrue(solve([0], 1))
        self.assertTrue(solve([0], 0))

    def test_edge_case_decreasing_sequence(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_invalid_input_non_list(self):
        self.assertRaises(TypeError, solve, 'not a list', 1)
