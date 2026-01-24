import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(shell_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([0, -1, -2]), [-2, -1, 0])

    def test_edge_case(self):
        self.assertEqual(shell_sort([]), [])
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([1, 1, 1]), [1, 1, 1])

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            shell_sort(123)
        with self.assertRaises(TypeError):
            shell_sort('123')
        with self.assertRaises(TypeError):
            shell_sort(None)
        with self.assertRaises(TypeError):
            shell_sort([1, 'a', None])
