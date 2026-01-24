import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, 3, 4]), 12)

    def test_zero_in_array(self):
        self.assertEqual(max_subarray_product([1, 2, 0, 3, 4]), 24)

    def test_all_zeroes(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0]), 0)

    def test_single_zero(self):
        self.assertEqual(max_subarray_product([0]), 0)

    def test_single_negative_number(self):
        self.assertEqual(max_subarray_product([-1]), -1)

    def test_empty_array(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_large_numbers(self):
        self.assertEqual(max_subarray_product([1000000, 2000000, 3000000, 4000000]), 12000000000000)

    def test_negative_and_large_numbers(self):
        self.assertEqual(max_subarray_product([-1000000, -2000000, 3000000, 4000000]), 12000000000000)
