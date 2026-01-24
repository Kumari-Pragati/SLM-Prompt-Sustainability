import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):
    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 3
        expected_output = [[1, 4], [1, 5], [1, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_boundary_case(self):
        nums1 = [1]
        nums2 = [4, 5, 6]
        k = 3
        expected_output = [[1, 4], [1, 5], [1, 6]]
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_edge_case(self):
        nums1 = []
        nums2 = [4, 5, 6]
        k = 3
        expected_output = []
        self.assertEqual(k_smallest_pairs(nums1, nums2, k), expected_output)

    def test_invalid_input(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        k = 'three'
        with self.assertRaises(TypeError):
            k_smallest_pairs(nums1, nums2, k)
