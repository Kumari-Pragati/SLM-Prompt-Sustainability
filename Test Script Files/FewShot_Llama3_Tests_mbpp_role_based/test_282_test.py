import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):
    def test_subtract_lists(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 1, 2]
        self.assertEqual(sub_list(nums1, nums2), [-1, 1, 1])

    def test_subtract_empty_list(self):
        nums1 = [1, 2, 3]
        nums2 = []
        self.assertEqual(sub_list(nums1, nums2), [1, 2, 3])

    def test_subtract_list_with_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 0, 0]
        self.assertEqual(sub_list(nums1, nums2), [1, 2, 3])

    def test_subtract_lists_with_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [1, 2, 3]
        self.assertEqual(sub_list(nums1, nums2), [-2, -4, -6])

    def test_subtract_lists_with_mixed_signs(self):
        nums1 = [1, -2, 3]
        nums2 = [0, 1, -2]
        self.assertEqual(sub_list(nums1, nums2), [1, -3, 5])
