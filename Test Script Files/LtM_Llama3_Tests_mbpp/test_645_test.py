import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 1), 30)

    def test_edge_case_empty(self):
        self.assertEqual(find_k_product([], 0), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_k_product([[1]], 0), 1)

    def test_edge_case_max_value(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 2), 6)

    def test_edge_case_min_value(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6]], 0), 1)

    def test_edge_case_negative(self):
        self.assertEqual(find_k_product([[-1, 2, 3], [4, 5, 6]], 1), 6)

    def test_edge_case_zero(self):
        self.assertEqual(find_k_product([[0, 2, 3], [4, 5, 6]], 1), 6)

    def test_edge_case_zero_product(self):
        self.assertEqual(find_k_product([[0, 0, 0], [4, 5, 6]], 1), 0)

    def test_edge_case_invalid_input(self):
        with self.assertRaises(IndexError):
            find_k_product([[1, 2, 3], [4, 5, 6]], 3)
