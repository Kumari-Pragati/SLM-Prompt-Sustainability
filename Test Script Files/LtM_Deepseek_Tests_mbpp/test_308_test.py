import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(large_product([1, 2], [3, 4], 2), [12, 8])
        self.assertEqual(large_product([-1, 2], [3, -4], 2), [-12, 8])

    def test_edge_conditions(self):
        self.assertEqual(large_product([], [], 0), [])
        self.assertEqual(large_product([1], [1], 1), [1])
        self.assertEqual(large_product([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), [25, 20, 18, 16, 15])

    def test_boundary_conditions(self):
        self.assertEqual(large_product([1000000000, 2000000000], [1000000000, 2000000000], 2), [4000000000000000000, 4000000000000000000])
        self.assertEqual(large_product([-1000000000, -2000000000], [-1000000000, -2000000000], 2), [4000000000000000000, 4000000000000000000])

    def test_complex_cases(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], 5), [25, 20, 18, 16, 15])
        self.assertEqual(large_product([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1], 5), [-1, -2, -3, -4, -5])
