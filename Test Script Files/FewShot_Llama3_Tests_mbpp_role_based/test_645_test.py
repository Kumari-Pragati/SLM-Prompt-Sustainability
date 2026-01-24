import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 1
        self.assertEqual(find_k_product(test_list, K), 3628800)

    def test_edge_case_empty_list(self):
        test_list = []
        K = 1
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_edge_case_single_element_list(self):
        test_list = [[1]]
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_edge_case_invalid_input(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 10
        with self.assertRaises(IndexError):
            find_k_product(test_list, K)
