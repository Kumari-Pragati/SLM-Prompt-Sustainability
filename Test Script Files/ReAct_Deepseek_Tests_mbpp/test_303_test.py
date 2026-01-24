import unittest
from mbpp_303_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_with_single_element(self):
        self.assertTrue(solve([1], 1))

    def test_edge_case_with_negative_numbers(self):
        self.assertTrue(solve([-1, -2, -3, -4, -5], 5))

    def test_edge_case_with_decreasing_sequence(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_edge_case_with_empty_list(self):
        self.assertTrue(solve([], 0))

    def test_error_case_with_invalid_input(self):
        with self.assertRaises(TypeError):
            solve("invalid input", 5)
