import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [10, 20, 30]
        nums2 = [1, 2, 3]
        expected_output = [10.0, 10.0, 10.0]
        self.assertEqual(div_list(nums1, nums2), expected_output)

    def test_edge_case_zero(self):
        nums1 = [10, 20, 30]
        nums2 = [0, 0, 0]
        expected_output = [float('inf'), float('inf'), float('inf')]
        self.assertEqual(div_list(nums1, nums2), expected_output)

    def test_boundary_case_single_element(self):
        nums1 = [10]
        nums2 = [1]
        expected_output = [10.0]
        self.assertEqual(div_list(nums1, nums2), expected_output)

    def test_special_case_negative_numbers(self):
        nums1 = [-10, -20, -30]
        nums2 = [1, 2, 3]
        expected_output = [-10.0, -10.0, -10.0]
        self.assertEqual(div_list(nums1, nums2), expected_output)

    def test_invalid_input_different_lengths(self):
        nums1 = [10, 20, 30]
        nums2 = [1, 2]
        with self.assertRaises(ValueError):
            div_list(nums1, nums2)

    def test_invalid_input_non_numeric(self):
        nums1 = [10, 20, 30]
        nums2 = ['a', 2, 3]
        with self.assertRaises(TypeError):
            div_list(nums1, nums2)
