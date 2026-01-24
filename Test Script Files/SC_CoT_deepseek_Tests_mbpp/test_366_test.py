import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 20)

    def test_single_element_list(self):
        self.assertEqual(adjacent_num_product([1]), 0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            adjacent_num_product([])

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -2)

    def test_large_numbers(self):
        self.assertEqual(adjacent_num_product([1000000, 2000000, 3000000]), 6000000000000)

    def test_zero_in_list(self):
        self.assertEqual(adjacent_num_product([1, 0, 3]), 0)

    def test_large_and_small_numbers(self):
        self.assertEqual(adjacent_num_product([-1000000, 2000000, -3000000]), -6000000000000)
