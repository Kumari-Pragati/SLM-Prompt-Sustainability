import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_with_negative_numbers(self):
        self.assertFalse(solve([5, 4, 3, 2, -1], 5))

    def test_edge_case_with_single_element(self):
        self.assertTrue(solve([5], 1))

    def test_edge_case_with_zero_elements(self):
        self.assertTrue(solve([], 0))

    def test_edge_case_with_maximum_value(self):
        self.assertTrue(solve([sys.maxsize], 1))

    def test_edge_case_with_minimum_value(self):
        self.assertFalse(solve([-sys.maxsize - 1], 1))

    def test_invalid_input_with_negative_n(self):
        with self.assertRaises(ValueError):
            solve([1, 2, 3, 4, 5], -1)

    def test_invalid_input_with_zero_n(self):
        self.assertTrue(solve([], 0))
