import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 1), 6)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 2), 18)
        self.assertEqual(find_k_product([[1], [2], [3]], 1), 2)
        self.assertEqual(find_k_product([[1], [2], [3]], 3), 6)

    def test_edge_cases(self):
        self.assertEqual(find_k_product([], 1), 1)
        self.assertEqual(find_k_product([[1]], 1), 1)
        self.assertEqual(find_k_product([[1], [2]], 0), 1)
        self.assertEqual(find_k_product([[1], [2]], 3), 2)

    def test_complex(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 72576)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 6)
