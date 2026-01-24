import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 120)
        self.assertEqual(max_subarray_product([10, -20, -30, 40]), 6000)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_subarray_product([-10, 20, -30, 40]), 6000)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-1, 2, -3, 4, -5]), 40)
        self.assertEqual(max_subarray_product([-10, 20, -30, 40]), 6000)

    def test_zeroes(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0]), 0)
        self.assertEqual(max_subarray_product([1, 2, 0, 3, 4]), 0)

    def test_single_number(self):
        self.assertEqual(max_subarray_product([5]), 5)
        self.assertEqual(max_subarray_product([0]), 0)
        self.assertEqual(max_subarray_product([-5]), -5)

    def test_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)
