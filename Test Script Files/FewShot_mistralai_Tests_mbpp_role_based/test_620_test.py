import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(largest_subset([]), 0)

    def test_single_element(self):
        self.assertEqual(largest_subset([1]), 1)

    def test_simple_sequence(self):
        self.assertEqual(largest_subset([1, 2, 3, 4]), 4)

    def test_duplicates(self):
        self.assertEqual(largest_subset([1, 1, 2, 3, 4]), 4)

    def test_all_multiples(self):
        self.assertEqual(largest_subset([2, 4, 6, 8]), 8)

    def test_all_primes(self):
        self.assertEqual(largest_subset([2, 3, 5, 7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(largest_subset([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_subset([1, -2, 3, -4, 5]), 5)
