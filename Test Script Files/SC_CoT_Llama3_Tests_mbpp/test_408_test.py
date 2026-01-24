import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_k_smallest_pairs_typical(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5], [1, 6]])

    def test_k_smallest_pairs_edge(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        k = 2
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5]])

    def test_k_smallest_pairs_edge2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 3], [1, 4], [2, 3]])

    def test_k_smallest_pairs_special(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 0
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [])

    def test_k_smallest_pairs_invalid(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = -1
        with self.assertRaises(ValueError):
            k_smallest_pairs(nums1, nums2, k)

    def test_k_smallest_pairs_empty(self):
        nums1 = []
        nums2 = [4, 5, 6]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [])

    def test_k_smallest_pairs_single(self):
        nums1 = [1, 2, 3]
        nums2 = []
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 0], [2, 0], [3, 0]])
