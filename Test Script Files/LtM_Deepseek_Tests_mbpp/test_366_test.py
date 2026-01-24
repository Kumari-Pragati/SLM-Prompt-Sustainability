import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), -6)
        self.assertEqual(adjacent_num_product([1, 0, 3, 4]), 0)

    def test_edge_conditions(self):
        self.assertEqual(adjacent_num_product([1]), 0)
        self.assertEqual(adjacent_num_product([]), 0)

    def test_complex_cases(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 12)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -12)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6]), 12)
