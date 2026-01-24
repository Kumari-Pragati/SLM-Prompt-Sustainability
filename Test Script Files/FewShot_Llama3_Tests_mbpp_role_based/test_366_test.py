import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)

    def test_edge_case_single_element_list(self):
        self.assertEqual(adjacent_num_product([1]), None)

    def test_edge_case_empty_list(self):
        self.assertEqual(adjacent_num_product([]), None)

    def test_edge_case_list_with_one_element(self):
        self.assertEqual(adjacent_num_product([1]), None)

    def test_edge_case_list_with_two_elements(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(adjacent_num_product([1, 1, 2, 2]), 4)

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), -6)
