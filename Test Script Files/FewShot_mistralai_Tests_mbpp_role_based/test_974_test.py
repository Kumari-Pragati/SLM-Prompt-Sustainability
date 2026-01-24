import unittest
from mbpp_974_code import min_sum_path

class TestMinSumPath(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_sum_path([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_sum_path([[1]]), 1)

    def test_simple_list(self):
        self.assertEqual(min_sum_path([[1, 2], [3, 4]]), 1)

    def test_list_with_zero(self):
        self.assertEqual(min_sum_path([[1, 0], [3, 4]]), 1)

    def test_list_with_negative_numbers(self):
        self.assertEqual(min_sum_path([[-1, -2], [-3, -4]]), -1)

    def test_list_with_large_numbers(self):
        self.assertEqual(min_sum_path([[1000000, 2], [3, 4]]), 2)

    def test_list_with_multiple_zeros(self):
        self.assertEqual(min_sum_path([[1, 0, 0], [3, 0, 4]]), 1)
