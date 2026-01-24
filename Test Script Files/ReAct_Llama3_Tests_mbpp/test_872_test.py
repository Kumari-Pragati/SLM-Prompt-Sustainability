import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], [2]))

    def test_multiple_element_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertFalse(check_subset([1, 2, 3], [4, 5]))

    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset([1, 1, 2, 2, 3], [1, 2]))

    def test_superset_with_duplicates(self):
        self.assertFalse(check_subset([1, 1, 2, 2, 3], [1, 1, 2, 3, 4]))

    def test_superset_with_duplicates_and_order_matters(self):
        self.assertFalse(check_subset([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_superset_with_duplicates_and_order_doesnt_matter(self):
        self.assertFalse(check_subset([1, 2, 3, 4], [1, 2, 3, 4]))

    def test_superset_with_duplicates_and_order_matters_and_duplicates(self):
        self.assertFalse(check_subset([1, 1, 2, 2, 3, 4], [4, 3, 2, 1, 1]))
