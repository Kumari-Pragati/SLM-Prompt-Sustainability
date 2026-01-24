import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_use_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 3
        self.assertEqual(large_product(nums1, nums2, N), [12, 10, 6])

    def test_edge_case_N_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 0
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_edge_case_N_greater_than_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 10
        self.assertEqual(large_product(nums1, nums2, N), sorted([x*y for x in nums1 for y in nums2], reverse=True))

    def test_invalid_input_type(self):
        nums1 = 'abc'
        nums2 = [4, 5, 6]
        N = 3
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)

    def test_invalid_input_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5]
        N = 3
        with self.assertRaises(IndexError):
            large_product(nums1, nums2, N)
