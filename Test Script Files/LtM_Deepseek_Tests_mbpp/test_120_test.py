import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 24)
        self.assertEqual(max_product_tuple([(-1, 2), (-3, 4), (-5, 6)]), 24)
        self.assertEqual(max_product_tuple([(1, -2), (3, -4), (5, -6)]), -24)

    def test_edge_conditions(self):
        self.assertEqual(max_product_tuple([(0, 1), (2, 3), (4, 5)]), 0)
        self.assertEqual(max_product_tuple([(-1, 0), (0, 1), (2, 3)]), 0)
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (0, 0)]), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_product_tuple([(1, 1), (1, 1), (1, 1)]), 1)
        self.assertEqual(max_product_tuple([(-1, -1), (-1, -1), (-1, -1)]), 1)
        self.assertEqual(max_product_tuple([(1, -1), (-1, 1), (1, -1)]), -1)

    def test_complex_cases(self):
        self.assertEqual(max_product_tuple([(1, 2), (-3, -4), (5, -6)]), 30)
        self.assertEqual(max_product_tuple([(-1, -2), (-3, 4), (5, 6)]), 30)
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (-5, -6)]), -30)
