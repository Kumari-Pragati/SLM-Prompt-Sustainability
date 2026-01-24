import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 45)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 36)

    def test_edge_conditions(self):
        self.assertEqual(find_k_product([], 0), 1)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 25)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), 36)

    def test_complex_cases(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 36)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 45)
