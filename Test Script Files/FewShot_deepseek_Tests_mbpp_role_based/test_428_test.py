import unittest
from mbpp_428_code import shell_sort

class TestShellSort(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(shell_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(shell_sort([5, 1, 4, 2, 8, 0]), [0, 1, 2, 4, 5, 8])

    def test_edge_conditions(self):
        self.assertEqual(shell_sort([1]), [1])
        self.assertEqual(shell_sort([]), [])

    def test_boundary_conditions(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            shell_sort(123)
        with self.assertRaises(TypeError):
            shell_sort('123')
        with self.assertRaises(TypeError):
            shell_sort(None)
        with self.assertRaises(TypeError):
            shell_sort([1, '2', 3])
