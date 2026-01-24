import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(shell_sort([3, 2, 1, 5, 4]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(shell_sort([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(shell_sort([-3, -2, -1, -5, -4]), [-5, -4, -3, -2, -1])

    def test_large_numbers(self):
        self.assertEqual(shell_sort([100, 200, 50, 300, 400]), [50, 100, 200, 300, 400])
