import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_simple_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 120)
        self.assertEqual(max_subarray_product([1, 2, 3]), 6)
        self.assertEqual(max_subarray_product([1]), 1)

    def test_simple_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -120)
        self.assertEqual(max_subarray_product([-1, -2, -3]), -6)
        self.assertEqual(max_subarray_product([-1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([1, -2, 3, -4, 5]), 15)
        self.assertEqual(max_subarray_product([-1, 2, -3, 4, -5]), -2)
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)

    def test_edge_cases(self):
        self.assertEqual(max_subarray_product([-1000000000]), -1000000000)
        self.assertEqual(max_subarray_product([1000000000]), 1000000000)
        self.assertEqual(max_subarray_product([-1000000000, -2000000000]), -2000000000)
        self.assertEqual(max_subarray_product([1000000000, 2000000000]), 2000000000)
