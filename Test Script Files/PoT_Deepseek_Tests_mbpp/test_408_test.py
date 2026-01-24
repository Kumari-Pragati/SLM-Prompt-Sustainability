import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5], [1, 6]])

    def test_edge_case_k_greater_than_total_pairs(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 6
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6]])

    def test_boundary_case_k_equals_total_pairs(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 6
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6]])

    def test_corner_case_empty_arrays(self):
        nums1 = []
        nums2 = [4, 5, 6]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [])

    def test_corner_case_one_element_arrays(self):
        nums1 = [1]
        nums2 = [4, 5, 6]
        k = 3
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 4], [1, 5], [1, 6]])

    def test_corner_case_same_elements_in_both_arrays(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3]
        k = 6
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3]])
