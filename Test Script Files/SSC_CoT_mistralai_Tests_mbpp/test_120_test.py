import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_product_tuple([1, 2, 3, 4]), 24)
        self.assertEqual(max_product_tuple([-1, -2, -3, -4]), 24)
        self.assertEqual(max_product_tuple([1, -1, 2, -2]), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_product_tuple([0, 0]), 0)
        self.assertEqual(max_product_tuple([0, 1]), 0)
        self.assertEqual(max_product_tuple([1, 0]), 0)
        self.assertEqual(max_product_tuple([1]), 1)
        self.assertEqual(max_product_tuple([-1]), 1)
        self.assertEqual(max_product_tuple([1, -1]), 1)
        self.assertEqual(max_product_tuple([-1, 1]), 1)

    def test_negative_list(self):
        self.assertEqual(max_product_tuple([-2, -3]), 6)
        self.assertEqual(max_product_tuple([-2, -3, 0]), 0)
        self.assertEqual(max_product_tuple([-2, 0, -3]), 0)
        self.assertEqual(max_product_tuple([0, -2, -3]), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, max_product_tuple, [1, 'a'])
        self.assertRaises(TypeError, max_product_tuple, ['a', 'b'])
