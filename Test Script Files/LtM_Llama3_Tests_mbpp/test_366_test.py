import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(adjacent_num_product([]), None)

    def test_single_element_input(self):
        self.assertEqual(adjacent_num_product([1]), None)

    def test_two_element_input(self):
        self.assertEqual(adjacent_num_product([1, 2]), 2)

    def test_three_element_input(self):
        self.assertEqual(adjacent_num_product([1, 2, 3]), 6)

    def test_max_product_at_start(self):
        self.assertEqual(adjient_num_product([3, 2, 1]), 6)

    def test_max_product_at_end(self):
        self.assertEqual(adjacent_num_product([1, 2, 3]), 6)

    def test_max_product_in_middle(self):
        self.assertEqual(adjacent_num_product([1, 3, 2]), 6)

    def test_max_product_at_start_and_end(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 12)

    def test_max_product_at_start_and_end_and_middle(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 30)
