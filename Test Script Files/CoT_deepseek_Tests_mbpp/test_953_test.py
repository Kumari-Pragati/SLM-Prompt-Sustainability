import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_single_element(self):
        self.assertEqual(subset([1], 1), 1)

    def test_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_repeated_elements(self):
        self.assertEqual(subset([1, 1, 1, 1], 4), 4)

    def test_sorted_array(self):
        self.assertEqual(subset([1, 2, 2, 3, 3, 3], 6), 3)

    def test_unsorted_array(self):
        self.assertEqual(subset([3, 2, 2, 1, 3, 3], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(subset([-1, -1, -1, 1, 1, 1], 6), 3)

    def test_mixed_numbers(self):
        self.assertEqual(subset([-1, 2, 2, 1, 3, 3], 6), 3)

    def test_large_numbers(self):
        self.assertEqual(subset([1000, 1000, 1000, 2000, 2000, 2000], 6), 3)
