import unittest
from mbpp_645_code import find_k_product, get_product

class TestFindKProduct(unittest.TestCase):

    def test_find_k_product_empty_list(self):
        test_list = []
        k = 0
        result = find_k_product(test_list, k)
        self.assertEqual(result, 1)

    def test_find_k_product_single_element(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        k = 2
        result = find_k_product(test_list, k)
        self.assertEqual(result, (get_product([2]) * get_product([6])))

    def test_find_k_product_multiple_elements(self):
        test_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        result = find_k_product(test_list, k)
        self.assertEqual(result, (get_product([1]) * get_product([3]) * get_product([9])))
