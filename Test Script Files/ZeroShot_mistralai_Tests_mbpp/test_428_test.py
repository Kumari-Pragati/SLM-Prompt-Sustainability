import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(shell_sort([1, 2, 3]), [1, 2, 3])

    def test_unsorted_list(self):
        unsorted_list = [5, 3, 8, 4, 2]
        sorted_list = [2, 3, 4, 5, 8]
        self.assertEqual(shell_sort(unsorted_list), sorted_list)

    def test_large_list(self):
        large_list = [1000, 999, 998, 997, 996]
        sorted_list = [996, 997, 998, 999, 1000]
        self.assertEqual(shell_sort(large_list), sorted_list)
