import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_find_k_product(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_k_product(test_list, 1), 3628800)
        self.assertEqual(find_k_product(test_list, 2), 3628800)
        self.assertEqual(find_k_product(test_list, 0), 3628800)

    def test_find_k_product_invalid_index(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(IndexError):
            find_k_product(test_list, 3)

    def test_find_k_product_empty_list(self):
        test_list = []
        with self.assertRaises(IndexError):
            find_k_product(test_list, 1)

    def test_find_k_product_single_element_list(self):
        test_list = [[1]]
        self.assertEqual(find_k_product(test_list, 0), 1)
