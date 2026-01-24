import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [30, 24])

    def test_edge_case_N_is_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 0
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_edge_case_N_is_greater_than_length_of_product_list(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 10
        self.assertEqual(large_product(nums1, nums2, N), sorted([x*y for x in nums1 for y in nums2], reverse=True))

    def test_edge_case_negative_numbers(self):
        nums1 = [-1, -2, -3]
        nums2 = [-4, -5, -6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [12, 10])

    def test_edge_case_one_empty_list(self):
        nums1 = []
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_edge_case_two_empty_lists(self):
        nums1 = []
        nums2 = []
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_edge_case_N_is_negative(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = -2
        with self.assertRaises(IndexError):
            large_product(nums1, nums2, N)
