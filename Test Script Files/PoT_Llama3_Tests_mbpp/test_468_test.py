import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 20)

    def test_edge_case_max_at_start(self):
        self.assertEqual(max_product([5, 1, 2, 3, 4], 5), 5)

    def test_edge_case_max_at_end(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_max_at_middle(self):
        self.assertEqual(max_product([1, 5, 2, 3, 4], 5), 20)

    def test_edge_case_single_element(self):
        self.assertEqual(max_product([5], 1), 5)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            max_product([], 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(max_product([-1, -2, -3, -4, -5], 5), -5)

    def test_edge_case_zero(self):
        self.assertEqual(max_product([0, 0, 0, 0, 0], 5), 0)
