import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 12)
        self.assertEqual(adjacent_num_product([2, 3, 4, 5]), 12)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 12)
        self.assertEqual(adjacent_num_product([1, 2, 3]), 6)
        self.assertEqual(adjacent_num_product([1, 2]), 2)
        self.assertEqual(adjacent_num_product([1]), 1)

    def test_zero(self):
        self.assertEqual(adjacent_num_product([0, 0]), 0)
        self.assertEqual(adjacent_num_product([0, 1]), 0)
        self.assertEqual(adjacent_num_product([0]), 0)

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), 12)
        self.assertEqual(adjacent_num_product([-1, -2, -3]), 6)
        self.assertEqual(adjacent_num_product([-1, -2]), 2)
        self.assertEqual(adjacent_num_product([-1]), 1)

    def test_empty_list(self):
        self.assertEqual(adjacent_num_product([]), None)

    def test_single_element_list(self):
        self.assertEqual(adjacent_num_product([1]), 1)
