import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_input(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_non_decreasing(self):
        self.assertTrue(check([1, 1, 1, 1, 1], 5))

    def test_edge_case_non_increasing(self):
        self.assertTrue(check([5, 4, 3, 2, 1], 5))

    def test_edge_case_decreasing(self):
        self.assertFalse(check([5, 4, 3, 2, 1], 5))

    def test_edge_case_increasing(self):
        self.assertFalse(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_equal(self):
        self.assertTrue(check([1, 1, 1, 1, 1], 5))

    def test_edge_case_negative(self):
        self.assertFalse(check([-5, -4, -3, -2, -1], 5))

    def test_edge_case_zero(self):
        self.assertTrue(check([0, 0, 0, 0, 0], 5))

    def test_edge_case_single_element(self):
        self.assertTrue(check([1], 1))

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            check([], 1)

    def test_edge_case_array_with_one_element(self):
        with self.assertRaises(IndexError):
            check([1], 0)
