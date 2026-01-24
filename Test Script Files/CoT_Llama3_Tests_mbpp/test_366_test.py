import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 6)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            adjacent_num_product([])

    def test_edge_case_single_element_list(self):
        with self.assertRaises(IndexError):
            adjacent_numProduct([1])

    def test_edge_case_two_element_list(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(adjacent_num_product([1, 2, 2, 3, 4]), 4)

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -6)

    def test_edge_case_list_with_mixed_signs(self):
        self.assertEqual(adjacent_num_product([1, -2, 3, -4, 5]), 6)
