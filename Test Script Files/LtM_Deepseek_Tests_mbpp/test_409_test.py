import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4)]), 2)
        self.assertEqual(min_product_tuple([(-1, 2), (3, -4)]), 4)

    def test_edge_conditions(self):
        self.assertEqual(min_product_tuple([(0, 1), (2, 3)]), 0)
        self.assertEqual(min_product_tuple([(-1, 0), (1, 0)]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(min_product_tuple([(1, 10**9), (-10**9, 1)]), 10**9)
        self.assertEqual(min_product_tuple([(-10**9, -1), (1, 10**9)]), -10**9)

    def test_complex_cases(self):
        self.assertEqual(min_product_tuple([(1, -2), (-3, 4)]), 6)
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4)]), 6)
