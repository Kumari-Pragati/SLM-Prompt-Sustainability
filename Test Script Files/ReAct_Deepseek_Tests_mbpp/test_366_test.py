import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 20)

    def test_single_element_list(self):
        self.assertEqual(adjacent_num_product([1]), 0)

    def test_empty_list(self):
        self.assertEqual(adjacent_num_product([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), -2)

    def test_zero_in_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 0, 4, 5]), 0)

    def test_large_numbers(self):
        self.assertEqual(adjacent_num_product([1000, 2000, 3000, 4000, 5000]), 2000000)

    def test_large_list(self):
        self.assertEqual(adjacent_num_product(list(range(1, 10001))), 9999999999)
