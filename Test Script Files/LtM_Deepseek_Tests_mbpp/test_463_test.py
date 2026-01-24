import unittest
from mbpp_463_code import max_subarray_product

class TestMaxSubarrayProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_subarray_product([1, 2, 3, 4]), 24)
        self.assertEqual(max_subarray_product([-1, -2, -3, -4]), -1)
        self.assertEqual(max_subarray_product([1, -2, 3, -4]), 12)

    def test_edge_conditions(self):
        self.assertEqual(max_subarray_product([0]), 0)
        self.assertEqual(max_subarray_product([1]), 1)
        self.assertEqual(max_subarray_product([-1]), -1)
        self.assertEqual(max_subarray_product([0, 0, 0]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_subarray_product([1, 0, -1]), 1)
        self.assertEqual(max_subarray_product([-1, 0, 1]), 0)
        self.assertEqual(max_subarray_product([-1, -2, -3, 0, -4]), 0)

    def test_complex_cases(self):
        self.assertEqual(max_subarray_product([-2, -3, 0, -4, -5]), 60)
        self.assertEqual(max_subarray_product([-2, -3, -1, -4, -5]), -6)
        self.assertEqual(max_subarray_product([-2, -3, -1, 0, -4, -5]), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_subarray_product("1, 2, 3, 4")
        with self.assertRaises(TypeError):
            max_subarray_product(1234)
        with self.assertRaises(TypeError):
            max_subarray_product(None)
