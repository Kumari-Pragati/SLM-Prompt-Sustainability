import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(adjacent_num_product([]))

    def test_single_element_list(self):
        self.assertIsNone(adjacent_num_product([1]))

    def test_two_elements_list(self):
        self.assertEqual(adjacent_num_product([2, 3]), 6)

    def test_three_elements_list(self):
        self.assertEqual(adjacent_num_product([2, 7, 11]), 88)

    def test_four_elements_list(self):
        self.assertEqual(adjacent_num_product([2, 7, 11, 19]), 152)

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-2, -7, -11, -19]), 288)

    def test_zero(self):
        self.assertIsNone(adjacent_num_product([0, 7, 11, 19]))
