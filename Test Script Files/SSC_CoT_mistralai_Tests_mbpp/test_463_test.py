import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20]), 1)
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 1209600)
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10]), 362880)

    def test_edge_case(self):
        self.assertEqual(max_subarray_product([]), 0)
        self.assertEqual(max_subarray_product([0]), 0)
        self.assertEqual(max_subarray_product([-1]), 1)
        self.assertEqual(max_subarray_product([-1, 0]), 1)
        self.assertEqual(max_subarray_product([0, -1]), 1)
        self.assertEqual(max_subarray_product([-1, 0, -1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_product([-1, -2, -3]), -6)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -8)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -10)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5, -6]), -12)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5, -6, -7]), -14)

    def test_positive_numbers(self):
        self.assertEqual(max_subarray_product([1, 2, 3]), 6)
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 60)
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5, 6]), 120)
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5, 6, 7]), 210)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3]), 6)
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3, -4]), 2)
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3, -4, 4]), 8)
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3, -4, 4, -5]), 4)
        self.assertEqual(max_subarray_product([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5]), 10)
