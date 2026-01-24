import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines_typical(self):
        self.assertTrue(parallel_lines([1, 2], [2, 3]))

    def test_parallel_lines_edge(self):
        self.assertTrue(parallel_lines([1, 1], [1, 1]))

    def test_parallel_lines_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            parallel_lines([1, 0], [2, 0])

    def test_parallel_lines_invalid_input_type(self):
        with self.assertRaises(TypeError):
            parallel_lines("1", [2, 3])

    def test_parallel_lines_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            parallel_lines([1, 2, 3], [4, 5, 6])

    def test_parallel_lines_non_parallel(self):
        self.assertFalse(parallel_lines([1, 2], [3, 4]))

    def test_parallel_lines_parallel(self):
        self.assertTrue(parallel_lines([1, 2], [1, 2]))
