import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_typical_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 1
        self.assertEqual(find_k_product(test_list, K), 3628800)

    def test_edge_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 0
        with self.assertRaises(IndexError):
            find_k_product(test_list, K)

    def test_edge_case2(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = len(test_list[0])
        self.assertEqual(find_k_product(test_list, K), 3628800)

    def test_special_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = len(test_list)
        self.assertEqual(find_k_product(test_list, K), 3628800)

    def test_invalid_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = -1
        with self.assertRaises(IndexError):
            find_k_product(test_list, K)
