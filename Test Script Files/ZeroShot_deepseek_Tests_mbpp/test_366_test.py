import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 20)

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(adjacent_num_product([-1, 2, -3, 4, -5]), 8)

    def test_single_number(self):
        self.assertEqual(adjacent_num_product([1]), 0)

    def test_empty_list(self):
        self.assertEqual(adjacent_num_product([]), 0)
