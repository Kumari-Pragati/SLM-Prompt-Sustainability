import unittest
from mbpp_651_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_subset_of_same_elements(self):
        self.assertTrue(check_subset((1, 2, 3), (1, 2, 3)))

    def test_subset_of_proper_elements(self):
        self.assertTrue(check_subset((1, 2, 3, 4), (1, 2, 3)))

    def test_subset_of_proper_elements_with_duplicates(self):
        self.assertTrue(check_subset((1, 1, 2, 3, 4), (1, 2, 3)))

    def test_subset_of_proper_elements_with_extra_elements(self):
        self.assertFalse(check_subset((1, 2, 3), (1, 2, 3, 4)))

    def test_subset_of_empty_sets(self):
        self.assertTrue(check_subset((), ()))

    def test_subset_of_empty_set_and_non_empty_set(self):
        self.assertFalse(check_subset((1, 2, 3), ()))

    def test_subset_of_non_empty_set_and_empty_set(self):
        self.assertFalse(check_subset((), (1, 2, 3)))

    def test_subset_of_sets_with_different_data_types(self):
        self.assertRaises(TypeError, check_subset, (1, 2, 3), (4, 'a', 5))
