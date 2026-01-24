import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_case(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 3
        expected = [12, 15, 18]
        self.assertEqual(large_product(nums1, nums2, N), expected)

    def test_edge_case_N_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 0
        self.assertEqual(large_product(nums1, nums2, N), [])

    def test_edge_case_N_greater_than_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 10
        expected = sorted([x*y for x in nums1 for y in nums2], reverse=True)
        self.assertEqual(large_product(nums1, nums2, N), expected[:N])

    def test_error_case_invalid_N_type(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 'a'
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)

    def test_error_case_invalid_input_type(self):
        nums1 = 'abc'
        nums2 = [4, 5, 6]
        N = 3
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)

    def test_edge_case_N_greater_than_length_with_duplicates(self):
        nums1 = [1, 2, 2]
        nums2 = [4, 5, 5]
        N = 5
        expected = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
        self.assertEqual(large_product(nums1, nums2, N), expected)
