import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([0, -1, -2, -3]), [-3, -2, -1, 0])

    def test_edge_conditions(self):
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([]), [])
        self.assertEqual(shell_sort([0]), [0])

    def test_complex_cases(self):
        self.assertEqual(shell_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(shell_sort([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(shell_sort([10, 9, 10, 9, 10]), [9, 9, 10, 10, 10])
