import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_subarray_product([2, 3, -2, 4]), 6)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -1)

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-2, -3, 0, 2, 3]), 6)

    def test_single_zero(self):
        self.assertEqual(max_subarray_product([0]), 0)

    def test_single_negative_number(self):
        self.assertEqual(max_subarray_product([-2]), -2)

    def test_single_positive_number(self):
        self.assertEqual(max_subarray_product([2]), 2)

    def test_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_large_numbers(self):
        self.assertEqual(max_subarray_product([1000000, -2, 300000, 400000]), 1200000000000)

    def test_large_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1000000, -2, -300000, -400000]), -1200000000000)

    def test_large_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-1000000, -2, 300000, 400000]), 1200000000000)

    def test_large_positive_numbers(self):
        self.assertEqual(max_subarray_product([1000000, 2, 300000, 400000]), 1200000000000)

    def test_large_zero(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0]), 0)

    def test_large_negative_zero(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, 0]), 0)

    def test_large_positive_zero(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 0]), 0)
