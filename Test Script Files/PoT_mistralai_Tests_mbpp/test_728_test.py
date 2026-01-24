import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_edge_case_empty_lists(self):
        self.assertEqual(sum_list([], []), [])

    def test_edge_case_different_lengths(self):
        self.assertEqual(sum_list([1, 2], [3, 4, 5]), [4, 6])

    def test_corner_case_negative_numbers(self):
        self.assertEqual(sum_list([-1, 2], [-3, 4]), [1, 6])
