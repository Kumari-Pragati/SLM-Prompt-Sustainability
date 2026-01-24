import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_check_subset_same_sets(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_check_subset_subset(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))

    def test_check_subset_disjoint_sets(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5, 6)))

    def test_check_subset_empty_sets(self):
        self.assertTrue(check_subset((), ()))

    def test_check_subset_one_empty_set(self):
        self.assertFalse(check_subset((1, 2, 3), ()))

    def test_check_subset_one_set_with_duplicates(self):
        self.assertTrue(check_subset((1, 1, 2), (1, 2)))

    def test_check_subset_one_set_with_no_duplicates_other_with_duplicates(self):
        self.assertFalse(check_subset((1, 2), (1, 1, 2)))

    def test_check_subset_one_set_with_no_elements(self):
        self.assertTrue(check_subset((), ()))
