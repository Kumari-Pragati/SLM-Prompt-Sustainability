import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [30, 24])

    def test_large_N(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 5
        self.assertEqual(large_product(nums1, nums2, N), [30, 24, 18, 15, 12])

    def test_empty_lists(self):
        nums1 = []
        nums2 = []
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [12, 15])

    def test_N_greater_than_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 10
        self.assertEqual(large_product(nums1, nums2, N), [30, 24, 18, 15, 12, 10, 9, 8, 7, 6])

    def test_single_number_lists(self):
        nums1 = [1]
        nums2 = [2]
        N = 1
        self.assertEqual(large_product(nums1, nums2, N), [2])

    def test_duplicate_numbers(self):
        nums1 = [1, 1, 1]
        nums2 = [2, 2, 2]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [6, 6])
