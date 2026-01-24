import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(largest_subset([]), 0)

    def test_single_element(self):
        self.assertEqual(largest_subset([1]), 1)

    def test_simple_case(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 2]), 3)

    def test_case_with_duplicates(self):
        self.assertEqual(largest_subset([1, 2, 2, 3, 4, 2]), 3)

    def test_case_with_zero(self):
        self.assertEqual(largest_subset([0, 1, 2, 3, 4]), 2)

    def test_case_with_negative_numbers(self):
        self.assertEqual(largest_subset([-1, -2, -3, -4]), 1)

    def test_case_with_large_numbers(self):
        self.assertEqual(largest_subset([1000000001, 1000000002, 1000000003, 1000000004]), 3)
