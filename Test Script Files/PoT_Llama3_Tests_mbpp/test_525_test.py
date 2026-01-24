import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(parallel_lines([1, 2], [3, 4]))

    def test_zero_slope(self):
        self.assertTrue(parallel_lines([0, 1], [0, 1]))

    def test_infinite_slope(self):
        self.assertTrue(parallel_lines([1, 0], [1, 0]))

    def test_non_parallel_lines(self):
        self.assertFalse(parallel_lines([1, 2], [2, 3]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            parallel_lines('a', [1, 2])

    def test_empty_input(self):
        with self.assertRaises(IndexError):
            parallel_lines([], [1, 2])

    def test_single_point_line(self):
        self.assertTrue(parallel_lines([1, 1], [1, 1]))

    def test_parallel_lines_with_zero_slope(self):
        self.assertTrue(parallel_lines([0, 1], [0, 1]))

    def test_non_parallel_lines_with_zero_slope(self):
        self.assertFalse(parallel_lines([0, 1], [1, 1]))
