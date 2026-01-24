import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_k_smallest_pairs_positive_numbers(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        expected = [[5, 6], [6, 5], [7, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected)

    def test_k_smallest_pairs_zero(self):
        nums1 = [0, 0]
        nums2 = [0, 0]
        k = 1
        expected = [[0, 0]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected)

    def test_k_smallest_pairs_k_greater_than_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 10
        expected = [[5, 6], [6, 5], [7, 6], [8, 6], [9, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected)

    def test_k_smallest_pairs_k_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 0
        expected = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected)

    def test_k_smallest_pairs_invalid_input(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = -1
        with self.assertRaises(ValueError):
            k_smallest_pairs(nums1, nums2, k)
