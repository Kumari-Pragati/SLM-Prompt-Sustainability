import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_max_subarray_product_positive(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 120)

    def test_max_subarray_product_negative(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)

    def test_max_subarray_product_mixed(self):
        self.assertEqual(max_subarray_product([1, -2, 3, 4, -5]), 4)

    def test_max_subarray_product_zero(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_max_subarray_product_empty(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_max_subarray_product_single_element(self):
        self.assertEqual(max_subarray_product([1]), 1)

    def test_max_subarray_product_all_negative(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)

    def test_max_subarray_product_all_positive(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 120)

    def test_max_subarray_product_mixed_with_zero(self):
        self.assertEqual(max_subarray_product([1, 0, -2, 3, 4]), 4)
