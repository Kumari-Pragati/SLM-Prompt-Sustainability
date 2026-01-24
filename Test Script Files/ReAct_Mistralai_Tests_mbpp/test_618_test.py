import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_div_list_positive_numbers(self):
        """Test div_list with positive numbers"""
        nums1 = [4, 8, 2]
        nums2 = [2, 4, 1]
        result = [2.0, 2.0, 2.0]
        self.assertListEqual(div_list(nums1, nums2), result)

    def test_div_list_mixed_numbers(self):
        """Test div_list with mixed numbers"""
        nums1 = [4, -8, 2, -2]
        nums2 = [2, -4, 1, -1]
        result = [2.0, -2.0, 2.0, -2.0]
        self.assertListEqual(div_list(nums1, nums2), result)

    def test_div_list_zero_denominator(self):
        """Test div_list with zero denominator"""
        nums1 = [1, 2, 3]
        nums2 = [0, 4, 1]
        with self.assertRaises(ZeroDivisionError):
            div_list(nums1, nums2)

    def test_div_list_empty_lists(self):
        """Test div_list with empty lists"""
        nums1 = []
        nums2 = [1, 2, 3]
        with self.assertRaises(ValueError):
            div_list(nums1, nums2)

        nums1 = [1, 2, 3]
        nums2 = []
        with self.assertRaises(ValueError):
            div_list(nums1, nums2)
