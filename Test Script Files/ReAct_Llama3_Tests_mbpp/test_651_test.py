import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2)))
    def test_not_subset(self):
        self.assertFalse(check_subset((1, 2, 3), (4, 5)))
    def test_empty_subset(self):
        self.assertTrue(check_subset((), ()))
    def test_empty_superset(self):
        self.assertFalse(check_subset((1, 2), ()))
    def test_single_element_subset(self):
        self.assertTrue(check_subset((1, 2, 3), (1)))
    def test_single_element_superset(self):
        self.assertFalse(check_subset((1), (1, 2, 3)))
    def test_subset_with_duplicates(self):
        self.assertTrue(check_subset((1, 2, 2, 3), (1, 2)))
    def test_superset_with_duplicates(self):
        self.assertFalse(check_subset((1, 2, 2, 3), (1, 2, 3, 4)))
