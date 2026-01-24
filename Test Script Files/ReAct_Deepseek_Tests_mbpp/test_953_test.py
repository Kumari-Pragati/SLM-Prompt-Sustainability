import unittest
from mbpp_953_code import subset

class TestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(subset([1, 2, 2, 3, 4], 5), 2)

    def test_single_element(self):
        self.assertEqual(subset([5], 1), 1)

    def test_repeated_elements(self):
        self.assertEqual(subset([1, 1, 1, 1, 1], 5), 5)

    def test_sorted_elements(self):
        self.assertEqual(subset([1, 2, 2, 3, 4], 5), 2)

    def test_unsorted_elements(self):
        self.assertEqual(subset([4, 2, 2, 3, 1], 5), 2)

    def test_empty_array(self):
        self.assertEqual(subset([], 0), 0)

    def test_negative_elements(self):
        self.assertEqual(subset([-1, -1, 1, 1, 1], 5), 2)

    def test_mixed_elements(self):
        self.assertEqual(subset([-1, 2, 2, 3, 4], 5), 2)

    def test_large_numbers(self):
        self.assertEqual(subset([10**6, 10**6, 10**6, 10**6, 10**6], 5), 5)
