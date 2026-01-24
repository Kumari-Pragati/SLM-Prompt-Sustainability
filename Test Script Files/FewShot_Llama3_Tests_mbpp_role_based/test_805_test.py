import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):
    def test_single_list(self):
        self.assertEqual(max_sum_list([[1, 2, 3]]), [1, 2, 3])

    def test_multiple_lists(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_empty_list(self):
        self.assertEqual(max_sum_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(max_sum_list([[1]]), [1])

    def test_negative_numbers(self):
        self.assertEqual(max_sum_list([[-1, -2, -3]]), [-1, -2, -3])

    def test_mixed_numbers(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, -5, 6], [7, 8, -9]]), [7, 8, -9])
