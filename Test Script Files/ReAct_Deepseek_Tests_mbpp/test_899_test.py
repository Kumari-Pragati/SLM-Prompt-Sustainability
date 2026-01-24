import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case_with_positive_numbers(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_typical_case_with_negative_numbers(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_typical_case_with_mixed_numbers(self):
        self.assertTrue(check([-1, 0, 1, 2, 3], 5))

    def test_edge_case_with_single_element(self):
        self.assertTrue(check([1], 1))

    def test_edge_case_with_zero_elements(self):
        self.assertTrue(check([], 0))

    def test_boundary_case_with_two_elements_increasing(self):
        self.assertTrue(check([1, 2], 2))

    def test_boundary_case_with_two_elements_decreasing(self):
        self.assertFalse(check([2, 1], 2))

    def test_boundary_case_with_two_elements_equal(self):
        self.assertTrue(check([1, 1], 2))

    def test_explicitly_handled_error_case_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            check([1, 'a', 2], 3)

    def test_explicitly_handled_error_case_with_negative_index(self):
        with self.assertRaises(IndexError):
            check([1, 2, 3], -1)
