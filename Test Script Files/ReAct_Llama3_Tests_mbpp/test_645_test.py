import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 1
        self.assertEqual(find_k_product(test_list, K), 3628800)

    def test_edge_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 3
        self.assertEqual(find_k_product(test_list, K), 6)

    def test_edge_case2(self):
        test_list = [[1, 2, 3]]
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_edge_case3(self):
        test_list = [[1, 2, 3]]
        K = 4
        self.assertRaises(IndexError, find_k_product, test_list, K)

    def test_empty_list(self):
        test_list = []
        K = 1
        self.assertRaises(IndexError, find_k_product, test_list, K)

    def test_single_sublist(self):
        test_list = [[1, 2, 3]]
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_single_sublist2(self):
        test_list = [[1, 2, 3]]
        K = 2
        self.assertEqual(find_k_product(test_list, K), 2)
