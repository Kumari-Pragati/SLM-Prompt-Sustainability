import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_edge_case_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_boundary_case_single_element(self):
        self.assertTrue(check_identical([1], [1]))

    def test_boundary_case_two_identical_lists(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_boundary_case_two_different_lists(self):
        self.assertFalse(check_identical([1, 2, 3], [3, 2, 1]))

    def test_error_handling_different_lengths(self):
        with self.assertRaises(AssertionError):
            check_identical([1, 2, 3], [1, 2])
