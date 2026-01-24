import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(shell_sort([5, 2, 8, 6, 1, 9]), [1, 2, 5, 6, 8, 9])

    def test_edge_case_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(shell_sort([5]), [5])

    def test_edge_case_sorted_list(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_reverse_sorted_list(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates(self):
        self.assertEqual(shell_sort([5, 2, 8, 6, 1, 9, 5, 2, 8, 6]), [1, 2, 2, 5, 5, 6, 6, 8, 8, 9])
