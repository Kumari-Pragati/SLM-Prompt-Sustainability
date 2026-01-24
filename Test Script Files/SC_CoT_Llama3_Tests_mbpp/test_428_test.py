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
        self.assertEqual(shell_sort([5, 2, 8, 3, 1, 6, 4]), [1, 2, 3, 4, 5, 6, 8])

    def test_duplicates_list(self):
        self.assertEqual(shell_sort([5, 2, 8, 3, 3, 1, 6, 4]), [1, 2, 3, 3, 4, 5, 6, 8])

    def test_large_list(self):
        self.assertEqual(shell_sort([5, 2, 8, 3, 3, 1, 6, 4, 7, 9, 10, 11, 12, 13, 14, 15]), [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            shell_sort("test")
