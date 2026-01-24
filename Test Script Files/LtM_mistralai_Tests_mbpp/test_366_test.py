import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 2 * 3)
        self.assertEqual(adjacent_num_product([5, 6, 7, 8]), 6 * 7)

    def test_edge_cases(self):
        self.assertEqual(adjacent_num_product([1]), 1)
        self.assertEqual(adjacent_num_product([1, 2]), 1 * 2)
        self.assertEqual(adjacent_num_product([1, 2, 3]), 1 * 2)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 2 * 3)

    def test_boundary_cases(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3]), (-1) * (-2))
        self.assertEqual(adjacent_num_product([0, 0, 0]), 0)
        self.assertEqual(adjacent_num_product([1000000000, 2000000000]), 1000000000 * 2000000000)

    def test_complex_cases(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6]), 2 * 3)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7]), 3 * 4)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8]), 4 * 5)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5 * 6)
