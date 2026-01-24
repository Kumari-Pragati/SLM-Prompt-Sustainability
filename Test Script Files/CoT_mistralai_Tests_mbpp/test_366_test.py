import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(adjacent_num_product([]))

    def test_single_element_list(self):
        self.assertIsNone(adjacent_num_product([1]))

    def test_simple_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 4)

    def test_list_with_zero(self):
        self.assertEqual(adjacent_num_product([0, 1, 2, 3]), 0)

    def test_list_with_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, 3, 4]), 12)

    def test_list_with_duplicates(self):
        self.assertEqual(adjacent_num_product([1, 1, 2, 3]), 2)

    def test_list_with_large_numbers(self):
        self.assertEqual(adjacent_num_product([1000000, 2000000, 3000000, 4000000]), 2400000000)
