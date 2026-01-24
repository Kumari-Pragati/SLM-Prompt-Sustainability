import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_with_single_element(self):
        self.assertTrue(check([1], 1))

    def test_edge_case_with_two_elements(self):
        self.assertTrue(check([1, 2], 2))

    def test_edge_case_with_two_same_elements(self):
        self.assertTrue(check([1, 1], 2))

    def test_edge_case_with_decreasing_elements(self):
        self.assertFalse(check([5, 4, 3, 2, 1], 5))

    def test_edge_case_with_increasing_elements(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_corner_case_with_negative_elements(self):
        self.assertTrue(check([-1, 0, 1, 2, 3], 5))

    def test_corner_case_with_zero_elements(self):
        self.assertTrue(check([0, 0, 0, 0, 0], 5))

    def test_invalid_input_n_less_than_2(self):
        with self.assertRaises(IndexError):
            check([1, 2, 3], 2)

    def test_invalid_input_empty_array(self):
        with self.assertRaises(IndexError):
            check([], 0)
