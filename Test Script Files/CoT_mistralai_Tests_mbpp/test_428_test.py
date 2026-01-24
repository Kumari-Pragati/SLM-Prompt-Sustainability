import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element_list(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(shell_sort([1, 2, 3]), [1, 2, 3])

    def test_reverse_sorted_list(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])

    def test_duplicate_elements(self):
        self.assertEqual(shell_sort([1, 1, 2, 3]), [1, 1, 2, 3])

    def test_large_list(self):
        large_list = [i for i in range(100)]
        sorted_list = sorted(large_list)
        self.assertEqual(shell_sort(large_list), sorted_list)

    def test_negative_numbers(self):
        self.assertEqual(shell_sort([-1, 0, 1]), [-1, 0, 1])

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            shell_sort([1, "a", 3.14])
