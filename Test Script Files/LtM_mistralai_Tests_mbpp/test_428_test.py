import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_simple_sort(self):
        self.assertEqual(shell_sort([1, 5, 2, 6, 3]), [1, 2, 3, 5, 6])
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([-1, 0, 1]), [-1, 0, 1])

    def test_edge_cases(self):
        self.assertEqual(shell_sort([]), [])
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([1, 1, 1]), [1, 1, 1])
        self.assertEqual(shell_sort([float('inf'), float('-inf')]), [float('-inf'), float('inf')])

    def test_complex_cases(self):
        self.assertEqual(shell_sort([5, 3, 4, 1, 6, 2]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shell_sort([-5, -3, -4, -1, -6, -2]), [-6, -5, -4, -3, -2, -1])
        self.assertEqual(shell_sort([1, 5, 2, 6, 3, 4]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(shell_sort([-1, 0, 1, 0, -1]), [-1, 0, 0, 1, -1])
