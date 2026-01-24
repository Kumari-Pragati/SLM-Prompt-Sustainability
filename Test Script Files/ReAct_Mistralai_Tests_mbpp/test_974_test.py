import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_sum_path([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_sum_path([[1]]), 1)

    def test_single_row_list(self):
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 1)

    def test_multi_row_list(self):
        self.assertEqual(min_sum_path([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)

    def test_negative_numbers(self):
        self.assertEqual(min_sum_path([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(min_sum_path([[1, -2, 3], [4, -5, 6], [7, -8, 9]]), 1)

    def test_all_zeroes(self):
        self.assertEqual(min_sum_path([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_single_column(self):
        self.assertEqual(min_sum_path([[1], [2], [3]]), 1)

    def test_single_row_and_column(self):
        self.assertEqual(min_sum_path([[1]]), 1)
