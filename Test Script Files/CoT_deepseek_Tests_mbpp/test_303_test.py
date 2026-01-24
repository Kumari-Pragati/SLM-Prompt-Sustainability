import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_smallest_number(self):
        self.assertTrue(solve([-1, 2, 3, 4, 5], 5))

    def test_edge_case_largest_number(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_edge_case_single_element(self):
        self.assertTrue(solve([1], 1))

    def test_edge_case_empty_list(self):
        self.assertTrue(solve([], 0))

    def test_invalid_input_negative_length(self):
        with self.assertRaises(ValueError):
            solve([1, 2, 3], -1)

    def test_invalid_input_non_integer_length(self):
        with self.assertRaises(TypeError):
            solve([1, 2, 3], 'a')
