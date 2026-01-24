import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(max_subarray_product([1, 2, -3, 4, -5, 6]), 6)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)
        self.assertEqual(max_subarray_product([1, 0, -1, 0, -1, 1]), 1)
        self.assertEqual(max_subarray_product([-1, 1, -1, 1, -1, 1]), 1)

    def test_edge_cases(self):
        self.assertEqual(max_subarray_product([]), 0)
        self.assertEqual(max_subarray_product([-1]), 0)
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([-1, 1]), 1)
        self.assertEqual(max_subarray_product([1, -1]), 1)
