import unittest
from mbpp_409_code import min_product_tuple

class TestMinProductTuple(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(min_product_tuple([(1, 2), (3, 4)]), min([abs(x * y) for x, y in [(1, 2), (3, 4)]]))
        self.assertEqual(min_product_tuple([(5, 6), (7, 8)]), min([abs(x * y) for x, y in [(5, 6), (7, 8)]]))
        self.assertEqual(min_product_tuple([(-1, 2), (3, -4)]), min([abs(x * y) for x, y in [(-1, 2), (3, -4)]]))

    def test_edge_cases(self):
        self.assertEqual(min_product_tuple([]), None)
        self.assertEqual(min_product_tuple([(0, 0)]), 0)
        self.assertEqual(min_product_tuple([(1, 0)]), 0)
        self.assertEqual(min_product_tuple([(0, 1)]), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            min_product_tuple('invalid_input')
