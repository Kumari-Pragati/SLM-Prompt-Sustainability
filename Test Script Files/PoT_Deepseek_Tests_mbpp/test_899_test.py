import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_with_single_element(self):
        self.assertTrue(check([1], 1))

    def test_boundary_case_with_two_elements(self):
        self.assertTrue(check([1, 2], 2))
        self.assertFalse(check([2, 1], 2))

    def test_boundary_case_with_three_elements(self):
        self.assertTrue(check([1, 2, 3], 3))
        self.assertFalse(check([3, 2, 1], 3))

    def test_corner_case_with_negative_numbers(self):
        self.assertTrue(check([-1, 0, 1], 3))
        self.assertFalse(check([1, 0, -1], 3))

    def test_corner_case_with_zero(self):
        self.assertTrue(check([0, 1, 2], 3))
        self.assertFalse(check([2, 1, 0], 3))

    def test_invalid_input_case_with_empty_array(self):
        with self.assertRaises(TypeError):
            check([], 0)

    def test_invalid_input_case_with_negative_length(self):
        with self.assertRaises(ValueError):
            check([1, 2, 3], -1)
