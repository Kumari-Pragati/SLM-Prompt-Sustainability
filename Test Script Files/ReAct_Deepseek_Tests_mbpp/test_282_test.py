import unittest
from mbpp_282_code import sub_list

class TestSubList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [10, 20, 30]
        nums2 = [5, 10, 15]
        expected_result = [5, 10, 15]
        self.assertEqual(sub_list(nums1, nums2), expected_result)

    def test_edge_case_with_negative_numbers(self):
        nums1 = [-10, -20, -30]
        nums2 = [-5, -10, -15]
        expected_result = [-5, -10, -15]
        self.assertEqual(sub_list(nums1, nums2), expected_result)

    def test_edge_case_with_zero(self):
        nums1 = [0, 0, 0]
        nums2 = [10, 20, 30]
        expected_result = [-10, -20, -30]
        self.assertEqual(sub_list(nums1, nums2), expected_result)

    def test_error_case_different_lengths(self):
        nums1 = [1, 2, 3, 4]
        nums2 = [1, 2, 3]
        with self.assertRaises(ValueError):
            sub_list(nums1, nums2)

    def test_error_case_non_numeric_input(self):
        nums1 = [1, 2, '3']
        nums2 = [1, 2, 3]
        with self.assertRaises(TypeError):
            sub_list(nums1, nums2)
