import unittest
from mbpp_682_code import mul_list

class TestMulList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected_output = [4, 10, 18]
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_edge_case_empty_lists(self):
        nums1 = []
        nums2 = []
        expected_output = []
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_edge_case_one_empty_list(self):
        nums1 = [1, 2, 3]
        nums2 = []
        expected_output = []
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_edge_case_one_number_in_list(self):
        nums1 = [1]
        nums2 = [2]
        expected_output = [2]
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_special_case_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [4, 5, 6]
        expected_output = [-4, -10, -18]
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_special_case_zero_in_list(self):
        nums1 = [1, 2, 3]
        nums2 = [0, 0, 0]
        expected_output = [0, 0, 0]
        self.assertEqual(mul_list(nums1, nums2), expected_output)

    def test_invalid_input_different_lengths(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        with self.assertRaises(ValueError):
            mul_list(nums1, nums2)
