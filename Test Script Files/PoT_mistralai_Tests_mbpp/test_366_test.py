import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 6)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), 10)
        self.assertEqual(adjacent_num_product([0, 1, 2, 3, 4]), 0)
        self.assertEqual(adjacent_num_product([10, 20, 30, 40, 50]), 600)

    def test_edge_case_single_element(self):
        self.assertEqual(adjacent_num_product([1]), 1)
        self.assertEqual(adjacent_num_product([1, ]), 1)
        self.assertEqual(adjacent_num_product([1, 2, ]), 2)
        self.assertEqual(adjacent_num_product([1, 2, 3, ]), 2)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, ]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(adjacent_num_product([]), None)
