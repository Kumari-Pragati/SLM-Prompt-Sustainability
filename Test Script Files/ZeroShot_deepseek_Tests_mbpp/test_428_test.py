import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([]), [])
        self.assertEqual(shell_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
