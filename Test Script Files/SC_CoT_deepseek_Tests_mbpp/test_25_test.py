import unittest

from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Product([2, 3, 4, 5], 4), 120)

    def test_single_element(self):
        self.assertEqual(find_Product([5], 1), 5)

    def test_duplicate_elements(self):
        self.assertEqual(find_Product([2, 2, 2, 2], 4), 4)

    def test_negative_numbers(self):
        self.assertEqual(find_Product([-2, -3, -4, -5], 4), -120)

    def test_zero(self):
        self.assertEqual(find_Product([0, 1, 2, 3], 4), 0)

    def test_large_numbers(self):
        self.assertEqual(find_Product([10**6, 10**6, 10**6], 3), 10**18)

    def test_sorted_array(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_unsorted_array(self):
        self.assertEqual(find_Product([5, 4, 3, 2, 1], 5), 120)

    def test_empty_array(self):
        with self.assertRaises(TypeError):
            find_Product([], 0)

    def test_negative_index(self):
        with self.assertRaises(IndexError):
            find_Product([1, 2, 3], -1)

    def test_large_index(self):
        with self.assertRaises(IndexError):
            find_Product([1, 2, 3], 4)
