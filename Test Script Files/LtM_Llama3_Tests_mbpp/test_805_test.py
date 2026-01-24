import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_empty_input(self):
        self.assertRaises(TypeError, max_sum_list, [])

    def test_single_list_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3]]), [1, 2, 3])

    def test_multiple_lists_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_negative_numbers_input(self):
        self.assertEqual(max_sum_list([[-1, -2, -3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_max_value_input(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), [10, 11, 12])

    def test_min_value_input(self):
        self.assertEqual(max_sum_list([[-1, -2, -3], [4, 5, 6], [7, 8, 9], [-10, -11, -12]]), [-10, -11, -12])
