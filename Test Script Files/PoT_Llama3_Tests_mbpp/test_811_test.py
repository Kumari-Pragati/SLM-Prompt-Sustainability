import unittest
from mbpp_811_code import check_identical

class TestCheckIdentical(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_identical([1, 2, 3], [1, 2, 3]))

    def test_edge_case_empty_lists(self):
        self.assertTrue(check_identical([], []))

    def test_edge_case_single_element_lists(self):
        self.assertTrue(check_identical([1], [1]))

    def test_edge_case_lists_of_different_lengths(self):
        self.assertFalse(check_identical([1, 2, 3], [1, 2]))

    def test_edge_case_lists_with_duplicates(self):
        self.assertTrue(check_identical([1, 2, 2, 3], [1, 2, 2, 3]))

    def test_edge_case_lists_with_duplicates_and_order_matters(self):
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 3, 2]))

    def test_edge_case_lists_with_duplicates_and_order_matters_and_empty(self):
        self.assertFalse(check_identical([1, 2, 2, 3], [1, 2]))

    def test_edge_case_lists_with_duplicates_and_order_matters_and_empty_and_empty(self):
        self.assertTrue(check_identical([], []))
