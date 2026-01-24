import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):
    def test_parallel_lines_positive(self):
        self.assertTrue(parallel_lines((1, 2), (3, 4)))
        self.assertTrue(parallel_lines((-1, 2), (3, 4)))
        self.assertTrue(parallel_lines((1, -2), (3, 4)))
        self.assertTrue(parallel_lines((1, 2), (-3, 4)))
        self.assertTrue(parallel_lines((1, 2), (3, -4)))

    def test_parallel_lines_zero_slope(self):
        self.assertTrue(parallel_lines((0, 1), (0, 2)))
        self.assertTrue(parallel_lines((0, -1), (0, 2)))
        self.assertTrue(parallel_lines((0, 1), (0, -2)))

    def test_parallel_lines_opposite_slope(self):
        self.assertFalse(parallel_lines((1, 2), (-1, 2)))
        self.assertFalse(parallel_lines((1, 2), (1, -2)))

    def test_parallel_lines_invalid_input(self):
        self.assertRaises(ValueError, parallel_lines, (0, 0), (0, 0))
        self.assertRaises(ValueError, parallel_lines, (0, 1), (0, 0))
        self.assertRaises(ValueError, parallel_lines, (0, 1), (0, -1))
