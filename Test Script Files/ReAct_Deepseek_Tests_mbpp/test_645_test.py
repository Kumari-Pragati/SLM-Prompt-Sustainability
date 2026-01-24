import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 1
        self.assertEqual(find_k_product(test_list, K), 40)

    def test_edge_case_k_zero(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_edge_case_k_negative(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = -1
        self.assertRaises(IndexError, find_k_product, test_list, K)

    def test_edge_case_k_greater_than_length(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 3
        self.assertRaises(IndexError, find_k_product, test_list, K)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)
