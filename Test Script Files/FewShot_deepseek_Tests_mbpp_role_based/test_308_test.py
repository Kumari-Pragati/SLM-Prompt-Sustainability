import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_use_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 2
        self.assertEqual(large_product(nums1, nums2, N), [30, 24])

    def test_edge_case_with_single_number(self):
        nums1 = [1]
        nums2 = [2]
        N = 1
        self.assertEqual(large_product(nums1, nums2, N), [2])

    def test_boundary_case_with_empty_lists(self):
        nums1 = []
        nums2 = []
        N = 0
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_boundary_case_with_one_empty_list(self):
        nums1 = []
        nums2 = [2, 3, 4]
        N = 3
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_invalid_input_N_greater_than_product_count(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 6
        with self.assertRaises(IndexError):
            large_product(nums1, nums2, N)
