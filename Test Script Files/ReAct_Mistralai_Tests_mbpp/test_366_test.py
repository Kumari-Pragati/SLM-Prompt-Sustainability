import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(adjacent_num_product([]))

    def test_single_element_list(self):
        self.assertIsNone(adjacent_num_product([1]))

    def test_two_elements_list(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_increasing_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 4)

    def test_decreasing_list(self):
        self.assertEqual(adjacent_num_product([4, 3, 2, 1]), 3)

    def test_alternating_list(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 10)

    def test_duplicates_in_list(self):
        self.assertEqual(adjacent_num_product([1, 1, 2, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(adjacent_num_product([-1, -2, -3]), 2)

    def test_zero_in_list(self):
        self.assertIsNone(adjacent_num_product([0, 1, 2]))
