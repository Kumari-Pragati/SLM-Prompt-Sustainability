import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_duplicate_elements(self):
        self.assertEqual(shell_sort([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(shell_sort([-3, -2, -1]), [-3, -2, -1])
        self.assertEqual(shell_sort([-5, -4, -3, -2, -1]), [-5, -4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(shell_sort([3, -2, 1]), [-2, 1, 3])
        self.assertEqual(shell_sort([5, 0, -3, 2, -1]), [-3, -1, 0, 2, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            shell_sort(123)
        with self.assertRaises(TypeError):
            shell_sort('123')
        with self.assertRaises(TypeError):
            shell_sort(None)
