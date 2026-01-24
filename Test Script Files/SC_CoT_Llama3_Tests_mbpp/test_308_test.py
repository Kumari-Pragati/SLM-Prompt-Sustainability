import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_inputs(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 3
        result = large_product(nums1, nums2, N)
        self.assertEqual(result, [18, 15, 12])

    def test_edge_case_N_zero(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 0
        result = large_product(nums1, nums2, N)
        self.assertEqual(result, [])

    def test_edge_case_N_greater_than_length(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 10
        result = large_product(nums1, nums2, N)
        self.assertEqual(result, sorted([x*y for x in nums1 for y in nums2], reverse=True))

    def test_invalid_input_non_integer_N(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        N = 'a'
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)

    def test_invalid_input_non_list_nums(self):
        nums1 = 'not a list'
        nums2 = [4, 5, 6]
        N = 3
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)

    def test_invalid_input_non_list_nums2(self):
        nums1 = [1, 2, 3]
        nums2 = 'not a list'
        N = 3
        with self.assertRaises(TypeError):
            large_product(nums1, nums2, N)
