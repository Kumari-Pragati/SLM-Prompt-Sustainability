import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(shell_sort([5, 3, 8, 6, 1, 9, 2, 7, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_single_element(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_edge_case_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_edge_case_duplicates(self):
        self.assertEqual(shell_sort([1, 1, 3, 8, 6, 1, 9, 2, 7, 4]), [1, 1, 2, 3, 4, 6, 7, 8, 9])

    def test_edge_case_reverse_order(self):
        self.assertEqual(shell_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_edge_case_all_same(self):
        self.assertEqual(shell_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(shell_sort([-5, -3, -8, -6, -1, -9, -2, -7, -4]), [-9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_edge_case_mixed_positive_negative(self):
        self.assertEqual(shell_sort([-5, 3, -8, 6, -1, 9, -2, 7, 4]), [-9, -8, -7, -6, -5, 1, 2, 4, 7])
