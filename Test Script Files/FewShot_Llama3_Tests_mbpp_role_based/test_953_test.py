import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):
    def test_subset_empty_array(self):
        self.assertEqual(subset([], 5), 0)

    def test_subset_single_element_array(self):
        self.assertEqual(subset([1], 5), 1)

    def test_subset_multiple_elements_array(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_subset_array_with_duplicates(self):
        self.assertEqual(subset([1, 1, 2, 2, 2, 3], 6), 3)

    def test_subset_array_with_no_duplicates(self):
        self.assertEqual(subset([1, 2, 3, 4, 5], 5), 1)

    def test_subset_array_with_negative_numbers(self):
        self.assertEqual(subset([-1, -2, -2, -3, -3, -3], 6), 3)

    def test_subset_array_with_zero(self):
        self.assertEqual(subset([0, 0, 0, 0, 0], 5), 1)

    def test_subset_array_with_negative_and_positive_numbers(self):
        self.assertEqual(subset([-1, 0, 0, 1, 1, 2], 6), 2)
