import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 1 * 2 * 3)
        self.assertEqual(find_k_product([[10, 20, 30], [40, 50, 60], [70, 80, 90]], 2), 20 * 30)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_k_product([], 1))

    def test_edge_case_empty_sublist(self):
        self.assertIsNone(find_k_product([[1], [], [3]], 1))

    def test_edge_case_k_greater_than_len(self):
        self.assertIsNone(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))

    def test_edge_case_k_less_than_0(self):
        self.assertIsNone(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1))
