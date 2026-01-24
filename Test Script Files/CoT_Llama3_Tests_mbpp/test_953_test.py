import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_subset_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_subset_single_element_array(self):
        self.assertEqual(subset([1], 1), 1)

    def test_subset_two_elements_array(self):
        self.assertEqual(subset([1, 2], 2), 1)

    def test_subset_three_elements_array(self):
        self.assertEqual(subset([1, 1, 2], 3), 2)

    def test_subset_four_elements_array(self):
        self.assertEqual(subset([1, 1, 2, 2], 4), 2)

    def test_subset_five_elements_array(self):
        self.assertEqual(subset([1, 1, 1, 2, 2], 5), 3)

    def test_subset_negative_elements_array(self):
        self.assertEqual(subset([-1, -1, -2, -2], 4), 2)

    def test_subset_zero_elements_array(self):
        self.assertEqual(subset([0, 0, 0], 3), 3)

    def test_subset_negative_and_positive_elements_array(self):
        self.assertEqual(subset([-1, -1, 1, 1], 4), 2)
