import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 3), 6)

    def test_edge_case(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)

    def test_edge_case2(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 1), 1)

    def test_edge_case3(self):
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 0), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_Product([], 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            find_Product([1, 2, 3, 4, 5], 'a')
