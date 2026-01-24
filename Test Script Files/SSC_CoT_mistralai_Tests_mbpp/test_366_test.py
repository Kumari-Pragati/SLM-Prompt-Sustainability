import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 6)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), 10)
        self.assertEqual(adjacent_num_product([0, 1, 2, 3, 4]), 0)

    def test_edge_cases(self):
        self.assertEqual(adjacent_num_product([1]), 1)
        self.assertEqual(adjacent_num_product([1, 2]), 2)
        self.assertEqual(adjacent_num_product([1, 2, 3]), 2)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7]), 14)

    def test_boundary_cases(self):
        self.assertEqual(adjacent_num_product([0, 0]), 0)
        self.assertEqual(adjacent_num_product([-1, 1]), 1)
        self.assertEqual(adjacent_num_product([1, -1]), 1)
