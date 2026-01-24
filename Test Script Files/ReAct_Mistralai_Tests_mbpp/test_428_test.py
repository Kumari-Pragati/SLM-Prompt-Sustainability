import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_empty_list(self):
        """Tests sorting an empty list"""
        result = shell_sort([])
        self.assertEqual(result, [])

    def test_single_element_list(self):
        """Tests sorting a list with one element"""
        result = shell_sort([42])
        self.assertEqual(result, [42])

    def test_sorted_list(self):
        """Tests sorting a sorted list"""
        result = shell_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """Tests sorting a reverse sorted list"""
        result = shell_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_duplicates(self):
        """Tests sorting a list with duplicates"""
        result = shell_sort([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
        self.assertEqual(result, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5])

    def test_large_list(self):
        """Tests sorting a large list"""
        result = shell_sort(list(range(100)))
        self.assertEqual(result, list(range(100)))

    def test_negative_numbers(self):
        """Tests sorting a list with negative numbers"""
        result = shell_sort([-1, -2, -3, 1, 2, 3])
        self.assertEqual(result, [-3, -2, -1, 1, 2, 3])

    def test_mixed_types(self):
        """Tests sorting a list with mixed types"""
        with self.assertRaises(TypeError):
            shell_sort([1, "a", 2, "b", 3])
