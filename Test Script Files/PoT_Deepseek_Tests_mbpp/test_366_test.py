import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 10)

    def test_edge_case_single_element(self):
        self.assertEqual(adjacent_num_product([1]), 0)

    def test_boundary_case_empty_list(self):
        self.assertEqual(adjacent_num_product([]), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -10)

    def test_corner_case_large_numbers(self):
        self.assertEqual(adjacent_num_product([1000000, 2000000, 3000000]), 2000000000000)
