import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        expected_output = [5, 7, 9]
        self.assertEqual(add_list(nums1, nums2), expected_output)

    def test_empty_lists(self):
        nums1 = []
        nums2 = []
        expected_output = []
        self.assertEqual(add_list(nums1, nums2), expected_output)

    def test_different_lengths(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        expected_output = [5, 7, 3]  # The shorter list is padded with zeros
        self.assertEqual(add_list(nums1, nums2), expected_output)

    def test_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        expected_output = [-5, -7, -9]
        self.assertEqual(add_list(nums1, nums2), expected_output)

    def test_large_numbers(self):
        nums1 = [1000000, 2000000, 3000000]
        nums2 = [4000000, 5000000, 6000000]
        expected_output = [5000000, 7000000, 9000000]
        self.assertEqual(add_list(nums1, nums2), expected_output)

    def test_invalid_input(self):
        nums1 = [1, 2, 3]
        nums2 = "not a list"
        with self.assertRaises(TypeError):
            add_list(nums1, nums2)
