import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [30, 24])

    def test_typical_case_with_duplicates(self):
        nums1 = [1, 2, 2]
        nums2 = [4, 5, 6]
        N = 3
        self.assertEqual(large_product(nums1, nums2, N), [30, 24, 20])

    def test_edge_case_with_large_numbers(self):
        nums1 = [10**6, 2*10**6]
        nums2 = [3*10**6, 4*10**6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [12*10**12, 8*10**12])

    def test_edge_case_with_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [-30, -24])

    def test_edge_case_with_zero(self):
        nums1 = [0, 2, 3]
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [0, 0])

    def test_error_case_with_empty_lists(self):
        nums1 = []
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_error_case_with_negative_N(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = -2
        with self.assertRaises(ValueError):
            large_product(nums1, nums2, N)
