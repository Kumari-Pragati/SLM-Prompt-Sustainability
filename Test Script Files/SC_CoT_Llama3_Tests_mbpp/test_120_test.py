import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4), (5, 6)]), 12)

    def test_edge_cases(self):
        self.assertEqual(max_product_tuple([(1, -1), (2, 3)]), 2)
        self.assertEqual(max_product_tuple([(1, 1), (2, 2)]), 4)

    def test_boundary_cases(self):
        self.assertEqual(max_product_tuple([(1, 0), (2, 0)]), 0)
        self.assertEqual(max_product_tuple([(0, 0), (0, 0)]), 0)

    def test_special_cases(self):
        self.assertEqual(max_product_tuple([(1, 1), (2, -2)]), 2)
        self.assertEqual(max_product_tuple([(1, -1), (2, 2)]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_product_tuple('invalid input')
