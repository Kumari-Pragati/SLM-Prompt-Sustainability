import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)

    def test_edge_case_single_element(self):
        self.assertRaises(IndexError, adjacent_num_product, [1])

    def test_edge_case_empty_list(self):
        self.assertRaises(IndexError, adjacent_num_product, [])

    def test_edge_case_two_elements(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2]), 2)

    def test_edge_case_positive_and_negative_numbers(self):
        self.assertEqual(adjacent_num_product([1, -2]), -2)

    def test_edge_case_all_positive_numbers(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 12)

    def test_edge_case_all_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), 4)
