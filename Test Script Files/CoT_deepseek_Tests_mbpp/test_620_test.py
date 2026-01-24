import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(largest_subset([10, 5, 20, 15], 4), 4)

    def test_single_element(self):
        self.assertEqual(largest_subset([1], 1), 1)

    def test_empty_list(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_all_divisible_pairs(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 5)

    def test_no_divisible_pairs(self):
        self.assertEqual(largest_subset([1, 3, 7, 9], 4), 1)

    def test_large_numbers(self):
        self.assertEqual(largest_subset([100, 200, 50, 150], 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(largest_subset([-10, -5, -20, -15], 4), 4)

    def test_duplicate_elements(self):
        self.assertEqual(largest_subset([10, 10, 20, 15], 4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_subset("10, 5, 20, 15", 4)
