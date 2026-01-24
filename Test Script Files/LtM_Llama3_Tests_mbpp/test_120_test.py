import unittest
from mbpp_120_code import max_product_tuple

class TestMaxProductTuple(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_product_tuple([(1, 2)]), 2)
        self.assertEqual(max_product_tuple([(-1, 2)]), 2)
        self.assertEqual(max_product_tuple([(1, -2)]), 2)
        self.assertEqual(max_product_tuple([(1, 1)]), 1)

    def test_edge(self):
        self.assertEqual(max_product_tuple([]), 0)
        self.assertEqual(max_product_tuple([(0, 0)]), 0)
        self.assertEqual(max_product_tuple([(0, 1)]), 0)
        self.assertEqual(max_product_tuple([(1, 0)]), 0)

    def test_max_product(self):
        self.assertEqual(max_product_tuple([(1, 2), (3, 4)]), 8)
        self.assertEqual(max_product_tuple([(-1, -2), (-3, -4)]), 4)
        self.assertEqual(max_product_tuple([(1, 2), (-3, 4)]), 8)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_product_tuple("Invalid input")
