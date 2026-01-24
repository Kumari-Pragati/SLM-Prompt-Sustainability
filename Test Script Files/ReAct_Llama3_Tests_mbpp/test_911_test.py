import unittest
from mbpp_911_code import maximum_product

class TestMaximumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5]), 60)

    def test_edge_case1(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5]), -60)

    def test_edge_case2(self):
        self.assertEqual(maximum_product([1, 1, 1, 1, 1]), 1)

    def test_edge_case3(self):
        self.assertEqual(maximum_product([-1, -1, -1, -1, -1]), -1)

    def test_edge_case4(self):
        self.assertEqual(maximum_product([1, 2, 3, 4, 5, 6]), 60)

    def test_edge_case5(self):
        self.assertEqual(maximum_product([-1, -2, -3, -4, -5, -6]), -60)

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            maximum_product('abc')

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            maximum_product([1, 2, '3', 4, 5])
