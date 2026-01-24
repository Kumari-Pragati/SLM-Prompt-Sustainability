import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):
    def test_division_by_non_zero(self):
        nums1 = [10, 20, 30]
        nums2 = [2, 4, 5]
        expected = [5.0, 5.0, 6.0]
        self.assertEqual(div_list(nums1, nums2), expected)

    def test_division_by_zero(self):
        nums1 = [10, 20, 30]
        nums2 = [0, 0, 0]
        with self.assertRaises(ZeroDivisionError):
            div_list(nums1, nums2)

    def test_division_by_negative(self):
        nums1 = [-10, -20, -30]
        nums2 = [2, 4, 5]
        expected = [-5.0, -5.0, -6.0]
        self.assertEqual(div_list(nums1, nums2), expected)

    def test_division_by_single_element(self):
        nums1 = [10]
        nums2 = [2]
        expected = [5.0]
        self.assertEqual(div_list(nums1, nums2), expected)

    def test_division_by_empty_lists(self):
        nums1 = []
        nums2 = []
        self.assertEqual(div_list(nums1, nums2), [])
