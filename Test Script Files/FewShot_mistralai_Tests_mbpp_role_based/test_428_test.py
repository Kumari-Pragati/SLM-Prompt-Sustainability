import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):
    def test_sorts_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_sorts_single_element_list(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_sorts_ascending_list(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorts_descending_list(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sorts_duplicate_elements(self):
        self.assertEqual(shell_sort([1, 1, 2, 3, 2]), [1, 1, 2, 2, 3])

    def test_sorts_large_list(self):
        large_list = [i for i in range(100)]
        sorted_list = sorted(large_list)
        self.assertEqual(shell_sort(large_list), sorted_list)

    def test_sorts_list_with_negative_numbers(self):
        self.assertEqual(shell_sort([-1, 0, 1]), [-1, 0, 1])

    def test_sorts_list_with_floats(self):
        self.assertEqual(shell_sort([1.1, 2.2, 3.3]), [1.1, 2.2, 3.3])
