import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_typical_use_case(self):
        nums1 = [10, 20, 30]
        nums2 = [2, 3, 4]
        expected_result = [0, 2, 0]
        self.assertEqual(moddiv_list(nums1, nums2), expected_result)

    def test_edge_case_zero_divisor(self):
        nums1 = [10, 20, 30]
        nums2 = [0, 0, 0]
        with self.assertRaises(ZeroDivisionError):
            moddiv_list(nums1, nums2)

    def test_edge_case_negative_numbers(self):
        nums1 = [-10, -20, -30]
        nums2 = [2, 3, 4]
        expected_result = [-1, -2, -0]
        self.assertEqual(moddiv_list(nums1, nums2), expected_result)

    def test_edge_case_single_element_lists(self):
        nums1 = [10]
        nums2 = [2]
        expected_result = [0]
        self.assertEqual(moddiv_list(nums1, nums2), expected_result)

    def test_edge_case_empty_lists(self):
        nums1 = []
        nums2 = []
        expected_result = []
        self.assertEqual(moddiv_list(nums1, nums2), expected_result)
