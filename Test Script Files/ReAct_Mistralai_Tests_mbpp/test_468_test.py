import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_empty_array(self):
        self.assertRaises(ValueError, max_product, [], 1)

    def test_single_element_array(self):
        self.assertEqual(max_product([1], 1), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 120)

    def test_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), 120)

    def test_mixed_numbers(self):
        self.assertEqual(max_product([1, -2, 3, -4, 5], 5), 15)

    def test_zero_in_array(self):
        self.assertEqual(max_product([0, 1, 2, 3, 4], 5), 0)

    def test_large_array(self):
        arr = [i for i in range(100)]
        self.assertEqual(max_product(arr, len(arr)), max(arr) * max(reversed(arr)))

    def test_negative_n(self):
        self.assertRaises(ValueError, max_product, [1, 2, 3], -1)
