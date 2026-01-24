import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):
    def test_typical_use_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        self.assertEqual(mul_list(nums1, nums2), [4, 10, 18])

    def test_edge_case_empty_lists(self):
        nums1 = []
        nums2 = []
        self.assertEqual(mul_list(nums1, nums2), [])

    def test_edge_case_single_element_lists(self):
        nums1 = [1]
        nums2 = [2]
        self.assertEqual(mul_list(nums1, nums2), [2])

    def test_edge_case_lists_of_different_lengths(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        self.assertEqual(mul_list(nums1, nums2), [4, 10])

    def test_edge_case_lists_with_negative_numbers(self):
        nums1 = [-1, 2, 3]
        nums2 = [4, -5, 6]
        self.assertEqual(mul_list(nums1, nums2), [-4, -10, 18])
