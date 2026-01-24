import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (-1, -2)]), 2)

    def test_edge_case(self):
        self.assertEqual(min_product_tuple([(0, 1), (2, 3), (-4, -5)]), 0)

    def test_boundary_case(self):
        self.assertEqual(min_product_tuple([(1, 1), (-1, -1)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_product_tuple([(-1, -2), (-3, -4), (1, 2)]), 4)

    def test_positive_numbers(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4), (-1, -2)]), 2)

    def test_zero(self):
        self.assertEqual(min_product_tuple([(0, 1), (2, 3), (0, -5)]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_product_tuple("invalid input")
