import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_empty_input(self):
        with self.assertRaises(IndexError):
            check([], 1)

    def test_edge_case_single_element_input(self):
        self.assertTrue(check([1], 1))

    def test_edge_case_two_elements_input(self):
        self.assertTrue(check([1, 2], 2))

    def test_edge_case_decreasing_sequence(self):
        self.assertFalse(check([5, 4, 3, 2, 1], 5))

    def test_edge_case_increasing_sequence(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_non_increasing_sequence(self):
        self.assertFalse(check([5, 3, 2, 1, 4], 5))

    def test_edge_case_non_decreasing_sequence(self):
        self.assertFalse(check([1, 3, 2, 4, 5], 5))

    def test_edge_case_negative_numbers(self):
        self.assertFalse(check([-5, -3, -2, -1], 4))

    def test_edge_case_positive_numbers(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_mixed_numbers(self):
        self.assertFalse(check([5, 3, 2, 1, 4], 5))
