import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_subset_with_same_elements(self):
        self.assertEqual(subset([1, 1, 1, 1], 4), 4)

    def test_subset_with_different_elements(self):
        self.assertEqual(subset([1, 2, 3, 4], 4), 1)

    def test_subset_with_repeated_elements(self):
        self.assertEqual(subset([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5], 11), 4)

    def test_subset_with_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_subset_with_empty_list(self):
        self.assertEqual(subset([], 0), 0)
