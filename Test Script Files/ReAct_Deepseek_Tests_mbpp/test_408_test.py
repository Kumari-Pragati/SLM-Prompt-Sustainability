import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        expected_output = [[1, 4], [1, 5], [1, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_typical_case_2(self):
        nums1 = [1, 1, 2]
        nums2 = [1, 2, 3]
        k = 2
        expected_output = [[1, 1], [1, 1]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_edge_case_k_greater_than_total_pairs(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        k = 5
        expected_output = [[1, 3], [1, 4], [2, 3], [2, 4]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_edge_case_empty_input(self):
        nums1 = []
        nums2 = [3, 4]
        k = 2
        expected_output = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_edge_case_one_empty_input(self):
        nums1 = [1, 2]
        nums2 = []
        k = 2
        expected_output = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)
