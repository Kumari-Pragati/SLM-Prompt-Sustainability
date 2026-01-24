import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(large_product([], [], 0), [])
        self.assertListEqual(large_product([], [1, 2, 3], 3), [])
        self.assertListEqual(large_product([1, 2, 3], [], 3), [])

    def test_single_element_lists(self):
        self.assertListEqual(large_product([1], [2, 3], 2), [2, 3])
        self.assertListEqual(large_product([2, 3], [1], 2), [2, 3])

    def test_small_lists(self):
        self.assertListEqual(large_product([1, 2], [3, 4], 2), [6, 4])
        self.assertListEqual(large_product([3, 4], [1, 2], 2), [6, 4])
        self.assertListEqual(large_product([1, 2], [3, 4], 3), [6, 4, 2])
        self.assertListEqual(large_product([3, 4], [1, 2], 3), [6, 4, 2])

    def test_large_lists(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [6, 7, 8, 9, 10]
        self.assertListEqual(large_product(nums1, nums2, 5), sorted([i*j for i in nums1 for j in nums2], reverse=True)[:5])
        self.assertListEqual(large_product(nums1, nums2, 10), sorted([i*j for i in nums1 for j in nums2], reverse=True)[:10])
