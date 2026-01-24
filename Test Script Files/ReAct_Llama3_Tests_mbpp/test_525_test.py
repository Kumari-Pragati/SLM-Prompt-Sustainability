import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines_typical(self):
        self.assertTrue(parallel_lines([1, 2], [3, 4]))

    def test_parallel_lines_zero_slope(self):
        self.assertTrue(parallel_lines([0, 1], [0, 1]))

    def test_parallel_lines_infinity_slope(self):
        self.assertTrue(parallel_lines([1, 0], [1, 0]))

    def test_parallel_lines_non_parallel(self):
        self.assertFalse(parallel_lines([1, 2], [3, 3]))

    def test_parallel_lines_zero_length(self):
        self.assertTrue(parallel_lines([0, 0], [0, 0]))

    def test_parallel_lines_invalid_input(self):
        with self.assertRaises(TypeError):
            parallel_lines('a', [1, 2])
