import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 3), [12, 15, 18])

    def test_edge_cases(self):
        self.assertEqual(large_product([1, 2], [3, 4], 2), [8, 6])
        self.assertEqual(large_product([1, 2, 3], [4], 1), [12])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            large_product(None, [1, 2, 3], 1)
        with self.assertRaises(TypeError):
            large_product([1, 2, 3], None, 1)
        with self.assertRaises(TypeError):
            large_product([1, 2, 3], [1, 2, 3], None)

    def test_boundary_conditions(self):
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 0), [])
        self.assertEqual(large_product([1, 2, 3], [4, 5, 6], 10), [])
