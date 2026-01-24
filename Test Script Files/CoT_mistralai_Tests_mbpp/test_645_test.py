import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_k_product([], 0))

    def test_single_element_list(self):
        self.assertEqual(find_k_product([{'a': 1}], 0), 1)
        self.assertEqual(find_k_product([{'a': 1}], 1), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(find_k_product([{'a': 1}, {'b': 2}], 0), 1)
        self.assertEqual(find_k_product([{'a': 1}, {'b': 2}], 1), 1)
        self.assertEqual(find_k_product([{'a': 1}, {'b': 2}], 2), 2)

    def test_negative_index(self):
        self.assertIsNone(find_k_product([{'a': 1}], -1))

    def test_out_of_range_index(self):
        self.assertIsNone(find_k_product([{'a': 1}, {'b': 2}], 3))

    def test_non_dict_element(self):
        self.assertIsNone(find_k_product([1, 2, 3], 0))
