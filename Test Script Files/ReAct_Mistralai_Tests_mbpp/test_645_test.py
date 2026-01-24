import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_find_k_product_positive(self):
        test_list = [
            {0: 1, 1: 2, 2: 3},
            {0: 4, 1: 5, 2: 6}
        ]
        K = 1
        expected = get_product([2, 6])
        self.assertEqual(find_k_product(test_list, K), expected)

    def test_find_k_product_zero(self):
        test_list = [
            {0: 1, 1: 0, 2: 3},
            {0: 4, 1: 0, 2: 6}
        ]
        K = 1
        self.assertEqual(find_k_product(test_list, K), 0)

    def test_find_k_product_negative(self):
        test_list = [
            {0: -1, 1: 2, 2: 3},
            {0: 4, 1: -5, 2: 6}
        ]
        K = 1
        expected = get_product([-1, -5])
        self.assertEqual(find_k_product(test_list, K), expected)

    def test_find_k_product_empty_list(self):
        test_list = []
        K = 0
        self.assertEqual(find_k_product(test_list, K), 1)

    def test_find_k_product_invalid_k(self):
        test_list = [
            {0: 1, 1: 2, 2: 3}
        ]
        K = 3
        with self.assertRaises(IndexError):
            find_k_product(test_list, K)
