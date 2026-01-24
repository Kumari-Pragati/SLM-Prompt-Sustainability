import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_sub_list_typical(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 1, 2]
        self.assertEqual(sub_list(nums1, nums2), [-1, 1, 1])

    def test_sub_list_edge(self):
        nums1 = [1, 2, 3]
        nums2 = [3, 2, 1]
        self.assertEqual(sub_list(nums1, nums2), [-2, 0, 2])

    def test_sub_list_empty(self):
        nums1 = []
        nums2 = [1, 2, 3]
        self.assertEqual(sub_list(nums1, nums2), [])

    def test_sub_list_single(self):
        nums1 = [1]
        nums2 = [1]
        self.assertEqual(sub_list(nums1, nums2), [])

    def test_sub_list_diff_len(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2]
        self.assertEqual(sub_list(nums1, nums2), [1, 1])

    def test_sub_list_negative(self):
        nums1 = [-1, 2, 3]
        nums2 = [1, 2, 3]
        self.assertEqual(sub_list(nums1, nums2), [-2, 0, 0])
