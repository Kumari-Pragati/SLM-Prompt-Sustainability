import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_empty_input(self):
        self.assertRaises(IndexError, min_sum_path, [])

    def test_single_element_input(self):
        self.assertEqual(min_sum_path([[1]]), 1)

    def test_two_element_input(self):
        self.assertEqual(min_sum_path([[1, 2], [3]]), 3)

    def test_three_element_input(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5], [6]]), 6)

    def test_edge_case_input(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5], [6, 7]]), 6)

    def test_negative_numbers_input(self):
        self.assertEqual(min_sum_path([[-1, 2, 3], [4, -5], [6, 7]]), 6)

    def test_max_value_input(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)

    def test_min_value_input(self):
        self.assertEqual(min_sum_path([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -9)
