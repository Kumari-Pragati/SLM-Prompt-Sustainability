import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)
        self.assertEqual(max_product([10, 20, 30, 40], 4), 4000)

    def test_edge_conditions(self):
        self.assertEqual(max_product([], 0), 0)
        self.assertEqual(max_product([1], 1), 1)
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -1)

    def test_boundary_conditions(self):
        self.assertEqual(max_product([1, 2, 3, 4], 4), 24)
        self.assertEqual(max_product([-1, -2, -3, -4], 4), -1)
        self.assertEqual(max_product([1, 2, 3, 0], 4), 0)

    def test_complex_cases(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 60)
        self.assertEqual(max_product([1, 2, 3, 4, -5], 5), 60)
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), -6)
