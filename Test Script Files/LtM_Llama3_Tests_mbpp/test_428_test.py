import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(shell_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(shell_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_duplicates(self):
        self.assertEqual(shell_sort([1, 2, 2, 3, 3, 3, 4, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5])

    def test_edge_case(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_max_value(self):
        self.assertEqual(shell_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_min_value(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
