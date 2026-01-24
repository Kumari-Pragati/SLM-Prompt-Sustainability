import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 15)
        self.assertEqual(max_subarray_product([10, 20, 30, 40, 50]), 150000)
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5, 6]), 720)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_subarray_product([-10, -20, -30, -40, -50]), -150000)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5, -6]), -720)

    def test_zero_numbers(self):
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)
        self.assertEqual(max_subarray_product([0, 0, 0, 1]), 1)
        self.assertEqual(max_subarray_product([0, 1, 0, -1]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([1, -2, 3, -4, 5]), 15)
        self.assertEqual(max_subarray_product([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_subarray_product([-1, 0, 1, 0, -1]), 1)

    def test_empty_list(self):
        self.assertEqual(max_subarray_product([]), 0)

    def test_single_number(self):
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([-1]), -1)
        self.assertEqual(max_subarray_product([0]), 0)
