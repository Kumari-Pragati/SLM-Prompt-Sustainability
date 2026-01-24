import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected_result = [4, 10, 18]
        self.assertEqual(mul_list(nums1, nums2), expected_result)

    def test_empty_lists(self):
        nums1 = []
        nums2 = []
        expected_result = []
        self.assertEqual(mul_list(nums1, nums2), expected_result)

    def test_one_empty_list(self):
        nums1 = [1, 2, 3]
        nums2 = []
        expected_result = []
        self.assertEqual(mul_list(nums1, nums2), expected_result)

    def test_different_lengths(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [5, 6]
        expected_result = [5, 12, 18]
        self.assertEqual(mul_list(nums1, nums2), expected_result)

    def test_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [4, 5, 6]
        expected_result = [-4, -10, -18]
        self.assertEqual(mul_list(nums1, nums2), expected_result)

    def test_zero(self):
        nums1 = [0, 2, 3]
        nums2 = [4, 5, 6]
        expected_result = [0, 10, 18]
        self.assertEqual(mul_list(nums1, nums2), expected_result)
