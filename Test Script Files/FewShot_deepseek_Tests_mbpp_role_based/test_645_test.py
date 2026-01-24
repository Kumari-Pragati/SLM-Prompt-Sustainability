import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 2
        self.assertEqual(find_k_product(test_list, K), 56)

    def test_edge_case_k_equals_zero(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_boundary_case_k_equals_length_of_sublist(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 3
        self.assertEqual(find_k_product(test_list, K), 0)

    def test_invalid_input_k_greater_than_length_of_sublist(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        K = 4
        with self.assertRaises(IndexError):
            find_k_product(test_list, K)
