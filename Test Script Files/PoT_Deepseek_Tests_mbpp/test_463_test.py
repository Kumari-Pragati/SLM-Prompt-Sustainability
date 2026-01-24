import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -1)
        self.assertEqual(max_subarray_product([-2, 3, -4, 5]), 60)
        self.assertEqual(max_subarray_product([0, 2, 3, 4]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([0]), 0)
        self.assertEqual(max_subarray_product([-1]), -1)
        self.assertEqual(max_subarray_product([-1, 0, 1]), 0)

    def test_corner_cases(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, 0, -4]), 0)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, 0]), 0)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -60)
