import unittest
from mbpp_303_code import solve

class TestSolve(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_edge_case_with_negative_numbers(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_boundary_case_with_single_element(self):
        self.assertTrue(solve([1], 1))

    def test_boundary_case_with_two_elements(self):
        self.assertTrue(solve([1, 2], 2))
        self.assertFalse(solve([2, 1], 2))

    def test_corner_case_with_sorted_descending_sequence(self):
        self.assertFalse(solve([5, 4, 3, 2, 1], 5))

    def test_corner_case_with_sorted_ascending_sequence(self):
        self.assertTrue(solve([1, 2, 3, 4, 5], 5))

    def test_invalid_input_case_with_empty_list(self):
        with self.assertRaises(TypeError):
            solve([], 0)

    def test_invalid_input_case_with_negative_n(self):
        with self.assertRaises(ValueError):
            solve([1, 2, 3, 4, 5], -1)
