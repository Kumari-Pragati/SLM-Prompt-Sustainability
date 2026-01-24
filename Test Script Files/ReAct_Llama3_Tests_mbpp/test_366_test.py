import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)

    def test_edge_case_empty_list(self):
        with self.assertRaises(IndexError):
            adjacent_num_product([])

    def test_edge_case_single_element_list(self):
        self.assertEqual(adjacent_num_product([1]), None)

    def test_edge_case_two_element_list(self):
        self.assertEqual(adjacent_num_product([1, 2]), None)

    def test_edge_case_three_element_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3]), 2)

    def test_edge_case_four_element_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)

    def test_edge_case_five_element_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 6)

    def test_edge_case_large_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 36)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), 2)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(adjacent_num_product([1, -2, 3, -4]), 12)
