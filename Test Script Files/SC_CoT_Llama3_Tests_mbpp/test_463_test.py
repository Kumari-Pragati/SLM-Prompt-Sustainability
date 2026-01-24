import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_typical_positive(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4, 5]), 60)

    def test_typical_negative(self):
        self.assertEqual(max_subarray_product([-1, -2, -3, -4, -5]), -60)

    def test_typical_zero(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_typical_mixed(self):
        self.assertEqual(max_subarray_product([1, -2, 3, 0, -4]), 12)

    def test_edge_all_positive(self):
        self.assertEqual(max_subarray_product([1, 1, 1, 1, 1]), 1)

    def test_edge_all_negative(self):
        self.assertEqual(max_subarray_product([-1, -1, -1, -1, -1]), -1)

    def test_edge_all_zero(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_edge_mixed_positive_negative(self):
        self.assertEqual(max_subarray_product([1, -2, 3, 0, -4]), 12)

    def test_edge_mixed_positive_zero(self):
        self.assertEqual(max_subarray_product([1, 0, 3, 0, -4]), 3)

    def test_edge_mixed_negative_zero(self):
        self.assertEqual(max_subarray_product([-1, 0, -3, 0, -4]), -4)

    def test_edge_mixed_zero(self):
        self.assertEqual(max_subarray_product([0, 0, 0, 0, 0]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_subarray_product("Invalid input")
