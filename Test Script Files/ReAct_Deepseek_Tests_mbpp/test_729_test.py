import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected_result = [5, 7, 9]
        self.assertEqual(add_list(nums1, nums2), expected_result)

    def test_empty_lists(self):
        nums1 = []
        nums2 = []
        expected_result = []
        self.assertEqual(add_list(nums1, nums2), expected_result)

    def test_different_lengths(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        expected_result = [5, 7, 3]
        self.assertEqual(add_list(nums1, nums2), expected_result)

    def test_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        expected_result = [-5, -7, -9]
        self.assertEqual(add_list(nums1, nums2), expected_result)

    def test_zeroes(self):
        nums1 = [0, 0, 0]
        nums2 = [0, 0, 0]
        expected_result = [0, 0, 0]
        self.assertEqual(add_list(nums1, nums2), expected_result)
