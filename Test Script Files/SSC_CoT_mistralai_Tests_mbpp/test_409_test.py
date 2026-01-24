import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (-5, 6)]), 60)
        self.assertEqual(min_product_tuple([(0, 0), (1, 2), (-5, 6)]), 0)
        self.assertEqual(min_product_tuple([(1, 0), (1, 2), (-5, 6)]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_product_tuple([(1, 0)]), 0)
        self.assertEqual(min_product_tuple([(0, 1)]), 0)
        self.assertEqual(min_product_tuple([(0, 0)]), 0)
        self.assertEqual(min_product_tuple([(-1, 1)]), 1)
        self.assertEqual(min_product_tuple([(1, -1)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4), (5, 6)]), 60)

    def test_empty_list(self):
        self.assertEqual(min_product_tuple([]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_product_tuple('string')
        with self.assertRaises(TypeError):
            min_product_tuple([1])
