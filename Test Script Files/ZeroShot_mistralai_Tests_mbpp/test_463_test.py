import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_single_element(self):
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([-1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([1, -2, 3, -4, 5]), 5)
        self.assertEqual(max_subarray_product([-1, 2, -3, 4, -5]), -4)
