import unittest
from mbpp_525_code import parallel_lines

class TestParallelLines(unittest.TestCase):

    def test_parallel_lines_positive(self):
        # Typical case: Two lines with the same slope
        self.assertTrue(parallel_lines((1, 2), (3, 6)))
        self.assertTrue(parallel_lines((-1, 2), (-3, -6)))
        self.assertTrue(parallel_lines((0, 1), (0, 2)))

    def test_parallel_lines_edge_cases(self):
        # Edge case: Two lines with zero slope
        self.assertTrue(parallel_lines((0, 0), (1, 0)))
        self.assertTrue(parallel_lines((0, 0), (0, 1)))

    def test_parallel_lines_different_slope(self):
        # Edge case: Two lines with different slopes
        self.assertFalse(parallel_lines((1, 2), (2, 3)))
        self.assertFalse(parallel_lines((-1, 2), (2, -3)))

    def test_parallel_lines_invalid_input(self):
        # Error case: Invalid input (non-parallel lines)
        self.assertRaises(ValueError, parallel_lines, (0, 0), (1, 0))
        self.assertRaises(ValueError, parallel_lines, (1, 0), (0, 0))
        self.assertRaises(ValueError, parallel_lines, (0, 0), (0, 0))
