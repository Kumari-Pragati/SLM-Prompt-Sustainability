import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 120)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, 3, 4, 5]), 120)

    def test_with_zero(self):
        self.assertEqual(max_subarray_product([-1, -2, 0, -4, -5]), 0)

    def test_with_single_element(self):
        self.assertEqual(max_subarray_product([5]), 5)

    def test_with_all_zeroes(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_with_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)
