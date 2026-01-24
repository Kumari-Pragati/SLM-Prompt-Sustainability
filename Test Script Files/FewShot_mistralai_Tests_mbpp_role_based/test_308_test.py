import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 10, 6])

    def test_empty_lists(self):
        self.assertEqual(large_product([], [], 0), [])
        self.assertEqual(large_product([], [], 1), [])
        self.assertEqual(large_product([], [1], 1), [])
        self.assertEqual(large_product([1], []), [])

    def test_single_element_lists(self):
        self.assertEqual(large_product([1], [2], 1), [2])
        self.assertEqual(large_product([1], [2], 2), [2, 1])

    def test_single_element_nums1(self):
        self.assertEqual(large_product([1], [2, 3], 1), [2])
        self.assertEqual(large_product([1], [2, 3], 2), [2, 3])

    def test_single_element_nums2(self):
        self.assertEqual(large_product([1, 2], [3], 1), [3])
        self.assertEqual(large_product([1, 2], [3], 2), [3, 2])

    def test_negative_numbers(self):
        self.assertEqual(large_product([-1, -2], [-3, -4], 2), [-4, -6])

    def test_large_numbers(self):
        self.assertEqual(large_product([1000000, 2000000], [3000000, 4000000], 1), [6000000000])
