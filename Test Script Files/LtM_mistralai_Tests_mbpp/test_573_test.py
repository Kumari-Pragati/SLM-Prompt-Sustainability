import unittest
from mbpp_573_code import unique_product

class TestUniqueProduct(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(unique_product([1, 2, 3]), 6)
        self.assertEqual(unique_product([-1, -2, -3]), 6)
        self.assertEqual(unique_product([0, 0, 0]), 0)

    def test_edge_input(self):
        self.assertEqual(unique_product([1]), 1)
        self.assertEqual(unique_product([1, 1]), 1)
        self.assertEqual(unique_product([-1, -1]), 1)
        self.assertEqual(unique_product([1, -1]), 1)
        self.assertEqual(unique_product([1, 0]), 1)
        self.assertEqual(unique_product([0, 1]), 1)

    def test_boundary_input(self):
        self.assertEqual(unique_product([-2147483648, -2147483647, -1]), -2147483648)
        self.assertEqual(unique_product([2147483647, 2147483648]), 2147483648)
        self.assertEqual(unique_product([-2147483648, -2147483647, 0]), 0)
        self.assertEqual(unique_product([2147483647, 2147483648, 0]), 0)

    def test_complex_input(self):
        self.assertEqual(unique_product([1, 2, 3, 2]), 6)
        self.assertEqual(unique_product([-1, -2, -3, -2]), 1)
        self.assertEqual(unique_product([0, 0, 1, 0]), 1)
