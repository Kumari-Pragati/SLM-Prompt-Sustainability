import unittest
from mbpp_729_code import add_list

class TestAddList(unittest.TestCase):
    def test_add_list_with_positive_numbers(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = add_list(nums1, nums2)
        self.assertEqual(result, [5, 7, 9])

    def test_add_list_with_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        result = add_list(nums1, nums2)
        self.assertEqual(result, [-5, -7, -9])

    def test_add_list_with_mixed_numbers(self):
        nums1 = [1, -2, 3]
        nums2 = [4, -5, 6]
        result = add_list(nums1, nums2)
        self.assertEqual(result, [5, -7, 9])

    def test_add_list_with_empty_list(self):
        nums1 = []
        nums2 = [1, 2, 3]
        result = add_list(nums1, nums2)
        self.assertEqual(result, [])

    def test_add_list_with_single_element_list(self):
        nums1 = [1]
        nums2 = [2]
        result = add_list(nums1, nums2)
        self.assertEqual(result, [3])
