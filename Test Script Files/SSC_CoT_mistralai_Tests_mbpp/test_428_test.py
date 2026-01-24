import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_sort_single_element_list(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_sort_simple_list(self):
        self.assertEqual(shell_sort([3, 5, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_sort_reverse_list(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sort_duplicates(self):
        self.assertEqual(shell_sort([3, 3, 5, 1, 4, 2]), [1, 2, 3, 3, 4, 5])

    def test_sort_large_list(self):
        self.assertEqual(shell_sort([10, 20, 30, 40, 50, 60, 70, 80, 90]), [10, 20, 30, 40, 50, 60, 70, 80, 90])

    def test_sort_list_with_zero(self):
        self.assertEqual(shell_sort([0, 1, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_sort_list_with_negative_numbers(self):
        self.assertEqual(shell_sort([-1, -2, 0, 1, 2]), [-1, -2, 0, 1, 2])

    def test_sort_list_with_floats(self):
        self.assertAlmostEqual(shell_sort([1.5, 2.5, 3.5]), [1.5, 2.5, 3.5])

    def test_sort_list_with_strings(self):
        self.assertEqual(shell_sort(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])
